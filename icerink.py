import pygame
import random
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, OFF_WHITE, BLUE, LIGHT_BLUE, DARK_RED

class IceRink:
    """
    Enhanced ice rink background with more realistic features.
    """
    def __init__(self, screen):
        self.screen = screen
        self.ice_color = OFF_WHITE 
        self.line_color = DARK_RED   
        self.blue_line_color = BLUE  
        self.crease_color = LIGHT_BLUE  

        # ice texture surface
        self.ice_texture = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        self.create_ice_texture()

    def create_ice_texture(self):
        for _ in range(10000):  # Adjust number of spots for desired density
            x = random.randint(0, SCREEN_WIDTH)
            y = random.randint(0, SCREEN_HEIGHT)
            radius = random.randint(1, 3)
            alpha = random.randint(10, 40)
            pygame.draw.circle(self.ice_texture, (255, 255, 255, alpha), (x, y), radius)

    def draw(self):
        # Fill background with ice color
        self.screen.fill(self.ice_color)
        
        # Apply ice texture
        self.screen.blit(self.ice_texture, (0, 0))

        # Draw center red line
        pygame.draw.line(self.screen, self.line_color, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT), 5)

        # Draw blue lines
        blue_line_offset = SCREEN_WIDTH // 3
        pygame.draw.line(self.screen, self.blue_line_color, (blue_line_offset, 0), (blue_line_offset, SCREEN_HEIGHT), 5)
        pygame.draw.line(self.screen, self.blue_line_color, (SCREEN_WIDTH - blue_line_offset, 0), (SCREEN_WIDTH - blue_line_offset, SCREEN_HEIGHT), 5)

        # Draw center face-off circle
        pygame.draw.circle(self.screen, self.line_color, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), 70, 5)

        # Draw other face-off circles
        circle_y = [SCREEN_HEIGHT // 4, 3 * SCREEN_HEIGHT // 4]
        circle_x = [SCREEN_WIDTH // 5, 4 * SCREEN_WIDTH // 5]
        for x in circle_x:
            for y in circle_y:
                pygame.draw.circle(self.screen, self.line_color, (x, y), 40, 5)

        # Draw goal creases
        crease_width = 90
        crease_height = 150
        pygame.draw.arc(self.screen, self.crease_color, (0, SCREEN_HEIGHT // 2 - crease_height // 2, crease_width, crease_height), -1.57, 1.57, 5)
        pygame.draw.arc(self.screen, self.crease_color, (SCREEN_WIDTH - crease_width, SCREEN_HEIGHT // 2 - crease_height // 2, crease_width, crease_height), 1.57, 4.71, 5)

        # Draw goal lines
        goal_line_offset = 40
        pygame.draw.line(self.screen, self.line_color, (goal_line_offset, 0), (goal_line_offset, SCREEN_HEIGHT), 5)
        pygame.draw.line(self.screen, self.line_color, (SCREEN_WIDTH - goal_line_offset, 0), (SCREEN_WIDTH - goal_line_offset, SCREEN_HEIGHT), 5)

        # Draw boards (as white lines around the edge)
        pygame.draw.rect(self.screen, (255, 255, 255), (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), 10)