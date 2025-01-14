from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract shape class.
    """
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    @abstractmethod
    def draw(self, screen):
        pass

    @abstractmethod
    def move(self):
        pass