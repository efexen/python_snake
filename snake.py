import pygame
from pygame.locals import *
from game_objects import *

class SnakeGame:

    def __init__(self, level):
        pygame.init()

        self.level = level
        self.snake = Snake(level)
        self.apple = Apple(level)

        self.screen = pygame.display.set_mode((level.width, level.height))
        self.running = True
        self.clock = pygame.time.Clock()
        self.score = 0

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
        elif event.key == K_ESCAPE:
            self.quit(event)

    def handle_event(self, event):
        {
            QUIT: self.quit,
            KEYDOWN: self.keydown
        }.get(event.type, lambda _: None)(event)

    def check_events(self):
        for event in pygame.event.get():
            self.handle_event(event)

    def update(self):
        self.snake.update()

    def draw_score(self):
        font = pygame.font.SysFont("comicsans", 28)
        text = font.render(str(self.score), True, (128, 128, 128))
        self.screen.blit(text, (0, 0))

    def draw(self):
        self.level.draw(self.screen)
        self.snake.draw(self.screen)
        self.apple.draw(self.screen)
        self.draw_score()

        pygame.display.flip()

    def eat_apple(self):
        self.apple = Apple(self.level)
        self.snake.grow()

        self.score += 100

    def check_collisions(self):

        if (((self.snake.x - 5 >= self.apple.x - 5
        and self.snake.x - 5 <= self.apple.x + 5)
        or (self.snake.x + 5 >= self.apple.x - 5
        and self.snake.x + 5 <= self.apple.x + 5))

        and ((self.snake.y - 5 >= self.apple.y - 5
        and self.snake.y - 5 <= self.apple.y + 5)
        or (self.snake.y + 5 >= self.apple.y - 5
        and self.snake.y + 5 <= self.apple.y + 5))):
            self.eat_apple()

    def play(self):
        while(self.running):
            self.check_events()
            self.check_collisions()
            self.update()
            self.draw()

            self.clock.tick(60)

level = Level(640, 480)
game = SnakeGame(level)
game.play()
