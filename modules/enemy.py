import pygame
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()

        # Charger l'image de l'ennemi
        self.image = pygame.image.load("assets/target.png")
        self.rect = self.image.get_rect()

        # Position initiale de l'ennemi (position aléatoire en haut de l'écran)
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = random.randint(-self.rect.height, 0)

        # Vitesse de déplacement de l'ennemi
        self.speed = 2

    def update(self):
        # Déplacer l'ennemi vers le bas (vers le joueur)
        self.rect.y += self.speed

    def draw(self, screen):
        # Afficher l'ennemi
        screen.blit(self.image, self.rect)

    def hit(self):
        # Faire disparaître l'ennemi lorsqu'il est touché par une balle
        self.kill()
        print("Ennemi touché !")
