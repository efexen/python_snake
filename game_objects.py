import pygame
import colorsys

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
        self.x = level.width // 2
        self.y = level.height // 2

        self.velocity_x = self.speed
        self.velocity_y = 0
        self.color = self.color_generator()

    def update(self):
        self.x += self.velocity_x
        self.y += self.velocity_y

    def color_generator(self):
        h = 0

        while True:
            r, g, b = colorsys.hls_to_rgb(h, 0.5, 1)
            yield tuple(i * 255 for i in (r, g, b))
            h += 0.001

    def draw(self, screen):
        print(next(self.color))
        pygame.draw.circle(screen, next(self.color), (self.x, self.y), 10, 2)
