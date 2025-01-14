import pygame
import random
import math
from shape import Shape
from constants import PUCK_SIZE, PUCK_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT

class Puck(Shape):
    """
    Puck class derived from Shape.
    """

    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = PUCK_SIZE // 2
        self.color = color
        self.speed = PUCK_SPEED / 3  # Initialize speed
        self.dx = 1
        self.dy = 0
        self.reset()

    @property
    def left(self):
        return self.x - self.radius

    @property
    def right(self):
        return self.x + self.radius

    @property
    def top(self):
        return self.y - self.radius

    @property
    def bottom(self):
        return self.y + self.radius

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)

    def reset(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2

        angle = random.uniform(-math.pi / 4, math.pi / 4)  # Random angle between -45 and 45 degrees

        if random.choice([True, False]):
            angle += math.pi

        self.speed = PUCK_SPEED / 3
        self.dx = self.speed * math.cos(angle)
        self.dy = self.speed * math.sin(angle)

    def collidesWithPaddle(self, paddle):
        # Using distance formula
        distance = math.hypot(self.x - paddle.x, self.y - paddle.y)
        return distance <= (self.radius + paddle.radius)

    def handlePaddleCollision(self, paddle):
        """
        Method that calculates the reflection of the puck when it collides with a paddle.
        """
        # Calculate the normal vector between puck and paddle
        normal_x = self.x - paddle.x
        normal_y = self.y - paddle.y

        # Normalize the normal vector
        normal_length = math.hypot(normal_x, normal_y)
        if normal_length == 0:
            normal_length = 1  # Prevent division by zero
        normal_x /= normal_length
        normal_y /= normal_length

        # Calculate the relative velocity
        rel_vel_x = self.dx - getattr(paddle, 'dx', 0)
        rel_vel_y = self.dy - getattr(paddle, 'dy', 0)

        # Dot product between relative velocity and normal
        dot_product = rel_vel_x * normal_x + rel_vel_y * normal_y

        # Reflect the velocity vector
        self.dx -= 2 * dot_product * normal_x
        self.dy -= 2 * dot_product * normal_y

        # Adjust speed to maintain consistent puck speed
        current_speed = math.hypot(self.dx, self.dy)
        if current_speed != 0:
            speed_ratio = self.speed / current_speed
            self.dx *= speed_ratio
            self.dy *= speed_ratio

        # Move puck slightly out of collision to prevent sticking
        overlap = (self.radius + paddle.radius) - normal_length + 1
        if overlap > 0:
            self.x += normal_x * overlap
            self.y += normal_y * overlap

    def update(self):
        self.move()

        # Apply minimal friction to simulate air hockey surface
        friction = 0.998
        self.dx *= friction
        self.dy *= friction

        # Ensure the puck doesn't slow down too much
        current_speed = math.hypot(self.dx, self.dy)
        min_speed = self.speed * 0.5
        if current_speed < min_speed:
            speed_ratio = min_speed / current_speed
            self.dx *= speed_ratio
            self.dy *= speed_ratio

        # Wall collision detection and response
        if self.left <= 0:
            self.x = self.radius
            self.dx *= -1
        elif self.right >= SCREEN_WIDTH:
            self.x = SCREEN_WIDTH - self.radius
            self.dx *= -1

        if self.top <= 0:
            self.y = self.radius
            self.dy *= -1
        elif self.bottom >= SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT - self.radius
            self.dy *= -1
    def get_position(self):
        """
        Return the current position of the puck. This was added for particle emission addition. 
        """
        return (self.x, self.y)
