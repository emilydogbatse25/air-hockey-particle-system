from shape import Shape
import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
import random

class Paddle(Shape):
    """
    Paddle class that works for Air Hockey instead of Pong. Paddles should be circles instead of Rectangles.
    """
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.dx = 0
        self.dy = 0

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)

    def move(self, dx, dy):
        
        new_x = self.x + dx
        new_y = self.y + dy
        
        
        # x-axis boundaries for collision
        if new_x - self.radius < 0:
            new_x = self.radius
        elif new_x + self.radius > SCREEN_WIDTH:
            new_x = SCREEN_WIDTH - self.radius

        # y-axis boundaries for collision
        if new_y - self.radius < 0:
            new_y = self.radius
        elif new_y + self.radius > SCREEN_HEIGHT:
            new_y = SCREEN_HEIGHT - self.radius
            
        self.x = new_x
        self.y = new_y

    def update(self):
       self.move(self.dx, self.dy)
        
    def reset_position(self, x, y):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0