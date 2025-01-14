import pygame
from constants import EMIT_RATE, PARTICLE_LIFESPAN
from particle import Particle
from complexparticle import ComplexParticle


class Emitter:
    """
    Emitter class emits the actual particles seen on the screen. 
    """
    def __init__(self, position, emit_rate):
        self.position = position  # Position where the particles are emitted
        self.emit_rate = emit_rate  # Emit rate in milliseconds
        self.particles = []  # List to hold particles
        self.last_emit_time = pygame.time.get_ticks()  # Track last time a particle was emitted
        self.particle_type = 'simple'
        
        
    def emit(self):
        """
        Emit new particles at regular intervals.
        Emit simple white particles or complex color-changing particles.
        """
        current_time = pygame.time.get_ticks()
        if current_time - self.last_emit_time > self.emit_rate:
            if self.particle_type == 'simple':
                # Emit a simple white particle
                new_particle = Particle(self.position, (0, 0, 102))
            elif self.particle_type == 'complex':
                # Emit a complex particle with varying size, color, and shape
                new_particle = ComplexParticle(self.position, lifespan=PARTICLE_LIFESPAN)

            # Add the new particle to the list
            self.particles.append(new_particle)
            self.last_emit_time = current_time


    def update(self):
        """
        removing the dead particles and updating the program
        """
        # Only keep particles that are still alive (update returns False if they should be removed)
        self.particles = [particle for particle in self.particles if particle.update()]

    def render(self, screen):
        """
        rendering all the particles
        """
        for particle in self.particles:
            particle.render(screen)
            
    def set_particle_type(self, particle_type):
        """
        Set the particle type to either 'simple' or 'complex'.
        """
        self.particle_type = particle_type
        
