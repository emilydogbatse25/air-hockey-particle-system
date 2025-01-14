import pygame
import random
from constants import PARTICLE_RADIUS, PARTICLE_TRANSPARENCY, PARTICLE_LIFESPAN, TRANSPARENCY_INC


class Particle:
    # constructor 
    def __init__(self, position, color, lifespan=PARTICLE_LIFESPAN):
        self.position = position  # x and y
        self.color = color  
        self.birth_time = pygame.time.get_ticks()  
        self.lifespan = lifespan  
        self.size = PARTICLE_RADIUS
        self.transparency = PARTICLE_TRANSPARENCY  # Full opacity at creation
        
    def age(self):
        """
        Returns the age of the particle in milliseconds.
        """
        return pygame.time.get_ticks() - self.birth_time
    
    def update(self):
        """Update the particle's transparency over time."""
        age = self.age()
        # Apply transparency decrement using TRANSPARENCY_INC
        self.transparency = max(self.transparency - TRANSPARENCY_INC, 0)

        # Return False if the particle has reached the end of its lifespan or is fully transparent
        return age <= self.lifespan and self.transparency > 0
    
    
    
    def render(self, screen):
        """
        method that just draws the particle 
        """
      
        # surface that accepts transparency 
        surface = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        
        
        particle_color = (*self.color, self.transparency)
        
        # drawing the actual particles on the screen
        pygame.draw.circle(surface, particle_color, (self.size // 2, self.size // 2), self.size // 2)
        
        # drawing the particle at the right position
        screen.blit(surface, (self.position[0] - self.size // 2, self.position[1] - self.size // 2))