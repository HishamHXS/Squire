import pygame

class Character:
    def __init__(self):
        self.sprite = pygame.Surface((50, 50))
        self.sprite.fill((255, 0, 0))  # Fill the sprite with red
        self.rect = self.sprite.get_rect()

    def move(self, dx, dy):
        self.rect.move_ip(dx, dy)

    def draw(self, screen):
        screen.blit(self.sprite, self.rect)