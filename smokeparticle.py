import pygame
import random

class SmokeParticle:
    def __init__(self, x, y, image, initial_velocity):
        self.x = x
        self.y = y
        self.scale_k = 0.1  # initial scale factor
        self.image = image
        self.alpha = 200  # Start a little transparent
        self.alpha_rate = 2  # decreases
        self.alive = True

        # Incorporate initial velocity with randomness
        self.vx = initial_velocity[0] * 0.2 + random.uniform(-0.5, 0.5)
        self.vy = initial_velocity[1] * 0.2 + random.uniform(-0.5, 0.5)

        self.drag = 0.92  # Slows down the particle over time

        # Random initial rotation angle and angular velocity
        self.angle = random.uniform(0, 360)
        self.angular_velocity = random.uniform(-1, 1)

    def update(self):
        # Update position
        self.x += self.vx
        self.y += self.vy

        # a little bit of a drag
        self.vx *= self.drag
        self.vy *= self.drag

        # upward movement
        self.vy -= 0.05  # can be adjusted

        # after some research smoke expands over time
        self.scale_k += 0.005  # adjust for desired amount

        # so that the smoke can fade out over time
        self.alpha -= self.alpha_rate
        if self.alpha <= 0:
            self.alpha = 0
            self.alive = False

        # Update the rotation angle
        self.angle += self.angular_velocity

    def draw(self, screen):
        # scaling and rotating
        scaled_image = pygame.transform.rotozoom(self.image, self.angle, self.scale_k)
        # usually wouldn't use the transform function by pygame, but this was my own addition to the project. 
        scaled_image.set_alpha(int(self.alpha))

        # Draw the image at the particle's position
        rect = scaled_image.get_rect(center=(self.x, self.y))
        screen.blit(scaled_image, rect)
