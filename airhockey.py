import pygame
from paddle import Paddle
from puck import Puck
from icerink import IceRink
from gamemanager import GameManager
from emitter import Emitter
from smoke import Smoke
from constants import (
    SCREEN_WIDTH, SCREEN_HEIGHT, PADDLE_SPEED,
    PADDLE_LEFT_COLOR, PADDLE_RIGHT_COLOR, WHITE,
    FPS, PADDLE_RADIUS, PUCK_SIZE, EMIT_RATE,
    KEY_PADDLE_LEFT_DOWN, KEY_PADDLE_LEFT_UP, KEY_PADDLE_RIGHT_DOWN, 
    KEY_PADDLE_RIGHT_UP, KEY_QUIT, KEY_RESET, KEY_START, 
    KEY_PADDLE_LEFT_LEFT, KEY_PADDLE_RIGHT_RIGHT, 
    KEY_PADDLE_RIGHT_LEFT, KEY_PADDLE_LEFT_RIGHT,
    KEY_NO_PARTICLES, KEY_SIMPLE_PARTICLES, KEY_COMPLEX_PARTICLES,
    KEY_SMOKE_PARTICLES, NAVY
)

class AirHockey:
    """
    Main air hockey class 
    """
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Project #2: Particle Systems")
        self.clock = pygame.time.Clock()

        # using the fonts
        self.font = pygame.font.Font('Minecraft.ttf', 32)
        self.title_font = pygame.font.Font('Minecraft.ttf', 46)

        self.paddle_left = Paddle(50, SCREEN_HEIGHT // 2, PADDLE_RADIUS, PADDLE_LEFT_COLOR)
        self.paddle_right = Paddle(SCREEN_WIDTH - 50, SCREEN_HEIGHT // 2, PADDLE_RADIUS, PADDLE_RIGHT_COLOR)
        self.puck = Puck(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, PUCK_SIZE // 2, NAVY)

        self.icerink = IceRink(self.screen)
        self.game_manager = GameManager(self.screen, self.font, self.title_font)
        
        # initialize all the particles
        self.emitter = Emitter(self.puck.get_position(), EMIT_RATE)
        self.smoke = Smoke(self.puck)
        
        self.particle_mode = 0  
        
        self.reset_game_objects()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.VIDEORESIZE:
                self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                self.game_manager.screen = self.screen
                self.icerink.screen = self.screen
            elif event.type == pygame.KEYDOWN:
                if event.key == KEY_QUIT:
                    return False
                elif event.key == KEY_RESET:
                    self.game_manager.resetGame()
                    self.reset_game_objects()
                elif event.key == KEY_START and self.game_manager.game_state in ["START", "ROUND_OVER", "GAME_OVER"]:
                    self.game_manager.startNextRoundOrGame()
                    self.reset_game_objects()
                elif event.key in [KEY_NO_PARTICLES, KEY_SIMPLE_PARTICLES, KEY_COMPLEX_PARTICLES, KEY_SMOKE_PARTICLES]:
                    self.set_particle_mode(event.key)

        if self.game_manager.game_state == "PLAYING":
            keys = pygame.key.get_pressed()
            
            # Left paddle movement (W, A, S, D)
            dx_left = dy_left = 0
            if keys[KEY_PADDLE_LEFT_UP]:    dy_left -= PADDLE_SPEED
            if keys[KEY_PADDLE_LEFT_DOWN]:  dy_left += PADDLE_SPEED
            if keys[KEY_PADDLE_LEFT_LEFT]:  dx_left -= PADDLE_SPEED
            if keys[KEY_PADDLE_LEFT_RIGHT]: dx_left += PADDLE_SPEED
            self.paddle_left.move(dx_left, dy_left)

            # Right paddle movement (I, J, K, L)
            dx_right = dy_right = 0
            if keys[KEY_PADDLE_RIGHT_UP]:    dy_right -= PADDLE_SPEED
            if keys[KEY_PADDLE_RIGHT_DOWN]:  dy_right += PADDLE_SPEED
            if keys[KEY_PADDLE_RIGHT_LEFT]:  dx_right -= PADDLE_SPEED
            if keys[KEY_PADDLE_RIGHT_RIGHT]: dx_right += PADDLE_SPEED
            self.paddle_right.move(dx_right, dy_right)

        return True

    def set_particle_mode(self, key):
        if key == KEY_NO_PARTICLES:
            self.particle_mode = 0
        elif key == KEY_SIMPLE_PARTICLES:
            self.particle_mode = 1
            self.emitter.set_particle_type('simple')
        elif key == KEY_COMPLEX_PARTICLES:
            self.particle_mode = 2
            self.emitter.set_particle_type('complex')
        elif key == KEY_SMOKE_PARTICLES:
            self.particle_mode = 3
        
        # particles should clear when switching between modes for visibility and functionality
        self.emitter.particles.clear()
        self.smoke.particles.clear()

    def reset_game_objects(self):
        self.puck.reset()
        self.paddle_left.x = 50
        self.paddle_left.y = SCREEN_HEIGHT // 2
        self.paddle_right.x = SCREEN_WIDTH - 50
        self.paddle_right.y = SCREEN_HEIGHT // 2
        
        self.emitter = Emitter(self.puck.get_position(), EMIT_RATE)
        self.smoke = Smoke(self.puck)

    def update(self):
        self.game_manager.update(self.puck, self.paddle_left, self.paddle_right)
        
        # update position of the emitter to follow the puck
        self.emitter.position = self.puck.get_position()

        # Emit and update particles based on the current mode
        if self.particle_mode in [1, 2]:  # simple or complex
            self.emitter.emit()
            self.emitter.update()
        elif self.particle_mode == 3:  # Smoke (not part of project)
            self.smoke.update()

    def draw(self):
        self.icerink.draw()
        if self.game_manager.game_state == "START":
            self.game_manager.drawStartScreen()
        elif self.game_manager.game_state in ["PLAYING", "ROUND_OVER"]:
            self.game_manager.drawGameScreen(self.paddle_left, self.paddle_right, self.puck)
            
            # draw the particles based on the mode
            if self.particle_mode in [1, 2]:
                self.emitter.render(self.screen)
            elif self.particle_mode == 3:
                self.smoke.draw(self.screen)

        elif self.game_manager.game_state == "GAME_OVER":
            self.game_manager.drawGameOverScreen()
        
        pygame.display.flip() # flip for the double buffering

# event loop 
    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)