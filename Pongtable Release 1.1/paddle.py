import pygame


class Paddle(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()

        self.color = color
        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, color, [0,0, width, height])

        self.rect = self.image.get_rect()

    def move_right(self, pixels, max_width):
        self.rect.x += pixels
        if self.rect.x > max_width:
            self.rect.x = max_width

    def move_left(self, pixels):
        self.rect.x -= pixels
        if self.rect.x < 0:
            self.rect.x = 0
