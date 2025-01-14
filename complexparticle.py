import pygame
import random
from constants import PALETTE, PARTICLE_LIFESPAN



class ComplexParticle:
    """
    This class represents an individual particle in the complex particle emission system.
    
    help from:
    https://github.com/kadir014/pygame-vfx/blob/main/src/fire.py
    """

    def __init__(self, position, lifespan=PARTICLE_LIFESPAN):
        # Apply symmetrical randomness to the initial position
        self.position = [
            position[0] + random.uniform(-5, 5),
            position[1] + random.uniform(-5, 5)
        ]
        self.lifespan = lifespan
        self.birth_time = pygame.time.get_ticks()
        self.size = random.uniform(15, 30)  # Increased size for larger particles
        self.initial_size = self.size  # Store initial size for reference
        self.life = self.lifespan  # Remaining life

        # random factors for the velocity
        self.velocity = [
            random.uniform(-0.5, 0.5),  
            random.uniform(-1.0, 1.0)  
        ]
        self.gravity = -0.02  # a little gravity 
        self.flicker = random.uniform(0.1, 0.5)  # Flickering effect

    def age(self):
        """Calculate the age of the particle."""
        return pygame.time.get_ticks() - self.birth_time

    def update(self):
        """Update the particle's state."""
        age = self.age()
        self.life = self.lifespan - age

        if self.life <= 0:
            return False  # Particle has expired

        life_fraction = self.life / self.lifespan  # Value between 0 and 1

        # Update position
        self.velocity[1] += self.gravity  # Apply gravity
        self.position[0] += self.velocity[0] + random.uniform(-self.flicker, self.flicker)
        self.position[1] += self.velocity[1]

        # Gradually reduce size
        self.size = self.initial_size * life_fraction  # Size decreases proportionally with life

        return True  # Particle is still alive

    def render(self, screen):
        """Render the particle onto the screen."""
        # Determine color based on life_fraction
        life_fraction = self.life / self.lifespan
        color_index = int((1 - life_fraction) * (len(PALETTE) - 1))
        color = PALETTE[color_index]

        # Alpha increases initially and then decreases
        if life_fraction > 0.5:
            alpha = int((1 - life_fraction) * 2 * 255)
        else:
            alpha = int(life_fraction * 2 * 255)
        alpha = max(0, min(alpha, 255))

        # Create a surface with per-pixel alpha
        surface_size = int(self.size * 4)
        particle_surface = pygame.Surface((surface_size, surface_size), pygame.SRCALPHA)

        # Draw multiple circles onto the surface to create a dense flame effect
        num_circles = 5  # Increased number of circles for density
        for _ in range(num_circles):
            offset_x = random.uniform(-self.size / 2, self.size / 2)
            offset_y = random.uniform(-self.size / 2, self.size / 2)
            circle_pos = (surface_size / 2 + offset_x, surface_size / 2 + offset_y)
            circle_size = self.size * random.uniform(0.5, 1.0)
            pygame.draw.circle(
                particle_surface,
                (*color, alpha),
                (int(circle_pos[0]), int(circle_pos[1])),
                int(circle_size)
            )

        # Blit the particle surface onto the main screen to handle transparency
        screen.blit(
            particle_surface,
            (self.position[0] - surface_size / 2, self.position[1] - surface_size / 2)
        )
