import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()

        # Charger l'image de la balle
        self.image = pygame.image.load("assets/rond.png")
        self.rect = self.image.get_rect()

        # Position initiale de la balle (hors de l'écran)
        self.rect.centerx = screen_width
        self.rect.bottom = screen_height

        # Vitesse de déplacement de la balle
        self.speed = 10

    def update(self):
        # Déplacer la balle vers le haut (vers les ennemis)
        self.rect.y -= self.speed

        # Vérifier si la balle est sortie de l'écran
        if self.rect.y < -self.rect.height:
            self.reset()

    def reset(self):
        # Réinitialiser la position de la balle (hors de l'écran)
        self.rect.x = -self.rect.width
        self.rect.y = -self.rect.height

    def fire(self, player):
        # Lorsque le joueur tire, positionner la balle au niveau du joueur
        self.rect.centerx = player.rect.centerx
        self.rect.top = player.rect.top

    def draw(self, screen):
        # Afficher la balle sur l'écran
        screen.blit(self.image, self.rect)
