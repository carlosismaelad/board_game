import pygame
import random
from pathlib import Path

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo do Dado")
clock = pygame.time.Clock()

# Carregando as imagens dos lados do dado

class Dado:
    def __init__(self):
        self.value = 1
        self.image = dice_images[self.value - 1]
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.rolling = False
        self.lados = [1, 2, 3, 4, 5, 6]

    def roll(self):
        self.rolling = True
        self.value = random.choice(self.lados)

    def update(self):
        if self.rolling:
            image_path = Path("assets/dices_side") / f"dice_{self.value}.png"
            self.image = pygame.image.load(str(image_path)).convert_alpha()
            self.rect = self.image.get_rect(center=(400, 300))
            self.rolling = False

    def draw(self, surface):
        if self.image is not None:
            surface.blit(self.image, self.rect)

dice_images = []
for i in range(1, 7):
    image_path = Path("assets/dices_side") / f"dice_{i}.png"
    image = pygame.image.load(str(image_path)).convert_alpha()
    dice_images.append(image)


