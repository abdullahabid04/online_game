import pygame

from Requirements import WIDTH, HEIGHT


class Player(object):
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.vel = 10

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.y -= self.vel
        if keys[pygame.K_DOWN]:
            self.y += self.vel
        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        self.check_bounds()
        self.update_rect()

    def check_bounds(self):
        if self.x < (self.width / 2):
            self.x = self.width / 2
        if self.x > (WIDTH - self.width * 2):
            self.x = WIDTH - self.width * 2
        if self.y < (self.height / 2):
            self.y = self.height / 2
        if self.y > (HEIGHT - self.height * 2):
            self.y = HEIGHT - self.height * 2

    def update_rect(self):
        self.rect = (self.x, self.y, self.width, self.height)
