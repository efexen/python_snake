import pygame
from pygame.locals import *
from game_objects import *

class SnakeGame:

    def __init__(self, level):
        pygame.init()

        self.level = level
        self.snake = Snake(level)

        self.game_objects = [self.level, self.snake]

        self.screen = pygame.display.set_mode((level.width, level.height))
        self.running = True
        self.clock = pygame.time.Clock()

    def quit(self, event):
        self.running = False

    def keydown(self, event):
        if event.key == K_LEFT:
            self.snake.velocity_x = -self.snake.speed
            self.snake.velocity_y = 0
        elif event.key == K_RIGHT:
            self.snake.velocity_x = self.snake.speed
            self.snake.velocity_y = 0
        elif event.key == K_UP:
            self.snake.velocity_y = -self.snake.speed
            self.snake.velocity_x = 0
        elif event.key == K_DOWN:
            self.snake.velocity_y = self.snake.speed
            self.snake.velocity_x = 0

    def handle_event(self, event):
        {
            QUIT: self.quit,
            KEYDOWN: self.keydown
        }.get(event.type, lambda _: None)(event)

    def check_events(self):
        for event in pygame.event.get():
            self.handle_event(event)

    def update(self):
        for game_object in self.game_objects:
            game_object.update()

    def draw(self):
        for game_object in self.game_objects:
            game_object.draw(self.screen)

        pygame.display.flip()

    def play(self):
        while(self.running):
            self.check_events()
            self.update()
            self.draw()

            self.clock.tick(60)

level = Level(640, 480)
game = SnakeGame(level)
game.play()
