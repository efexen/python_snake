import pygame
import colorsys
from random import randint

class Apple:

    def __init__(self, level):
        self.x = randint(20, level.width - 20)
        self.y = randint(20, level.height - 20)

        print("New apple :o", self.x, self.y)

    def update(self):
        pass

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 255, 0), (self.x, self.y), 10, 0)


class Level:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def update(self):
        pass

    def draw(self, screen):
        screen.fill((0, 0, 0))

class Snake:

    speed = 2

    def __init__(self, level):
        self.segments = []

        self.x = level.width // 2
        self.y = level.height // 2

        self.segments.append((self.x, self.y))

        self.velocity_x = self.speed
        self.velocity_y = 0
        self.color_seq = 0

    def grow(self):
        for _ in range(10):
            self.segments.insert(-1, self.segments[-1])

    def update(self):
        self.x += self.velocity_x
        self.y += self.velocity_y
        self.color_seq += 0.01

        self.segments.insert(0, (self.x, self.y, self.color_seq))
        self.segments.pop()

    def color_for(self, seq):
        r, g, b = colorsys.hls_to_rgb(seq, 0.5, 1)
        return tuple(i * 255 for i in (r, g, b))

    def draw(self, screen):
        for x, y, color in self.segments:
            pygame.draw.circle(screen, self.color_for(color), (x, y), 10, 0)
