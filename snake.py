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
        self.playing = True
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

    def draw_score_screen(self):
        font = pygame.font.SysFont("comicsans", 56)
        text = font.render("Game Over", True, (128, 0, 0))
        center_x = self.level.width // 2
        center_y = self.level.height // 2
        self.screen.blit(text, (center_x - text.get_width() // 2, center_y - text.get_height() // 2))

    def draw(self):
        self.level.draw(self.screen)
        self.snake.draw(self.screen)
        self.apple.draw(self.screen)
        self.draw_score()

        if not self.playing:
            self.draw_score_screen()

        pygame.display.flip()

    def eat_apple(self):
        self.apple = Apple(self.level)
        self.snake.grow()

        self.score += 100

    def game_over(self):
        self.playing = False

    def check_collisions(self):
        checker = CollisionChecker()

        if checker.collided(self.snake, self.apple, 2):
            self.eat_apple()

        if checker.out_of_bounds(self.snake, self.level):
            self.game_over()


    def play(self):
        while(self.running):
            if (self.playing):
                self.check_collisions()
                self.update()

            self.check_events()
            self.draw()
            self.clock.tick(60)

level = Level(640, 480)
game = SnakeGame(level)
game.play()
