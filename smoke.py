import pygame
import math
import random
from smokeparticle import SmokeParticle

class Smoke:
    def __init__(self, ball):
        self.ball = ball
        self.particles = []
        self.last_position = (ball.x, ball.y)
        self.load_image()

    def load_image(self):
        try:
            self.image = pygame.image.load('smoke.png').convert_alpha()
        except pygame.error:
            print("Error: Unable to load smoke texture.")
            self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
            pygame.draw.circle(self.image, (200, 200, 200, 128), (25, 25), 25)

    def update(self):
        current_position = (self.ball.x, self.ball.y)
        velocity = (
            current_position[0] - self.last_position[0],
            current_position[1] - self.last_position[1]
        )
        speed = math.hypot(*velocity)

        # Emit particles based on ball's speed
        if speed > 0.5:  # Adjust this threshold as needed
            num_particles = int(speed / 2)  # Adjust this ratio for desired density
            for _ in range(num_particles):
                offset_x = random.uniform(-5, 5)
                offset_y = random.uniform(-5, 5)
                particle_x = self.ball.x + offset_x
                particle_y = self.ball.y + offset_y
                self.particles.append(SmokeParticle(particle_x, particle_y, self.image, velocity))

        self.particles = [p for p in self.particles if p.alive]
        for p in self.particles:
            p.update()

        self.last_position = current_position

    def draw(self, screen):
        for p in self.particles:
            p.draw(screen)