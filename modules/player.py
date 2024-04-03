import pygame
from modules.bullet import Bullet


class Player(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()

        self.screen_width = screen_width
        # Ajoutez un attribut pour gérer les ennemis touchés
        self.enemies_hit = pygame.sprite.Group()

        # Charger l'image du vaisseau spatial
        self.image = pygame.image.load("assets/fusee.png")
        self.rect = self.image.get_rect()

        # Position initiale du joueur
        self.rect.centerx = screen_width // 2
        self.rect.bottom = screen_height - 10

        # Vitesse de déplacement du joueur
        self.speed = 10

        # Créer une liste pour stocker les balles
        self.bullets = pygame.sprite.Group()

        # Ajoutez un attribut pour gérer le délai entre les tirs
        # Délai en nombre de frames (modifiable selon vos préférences)
        self.fire_delay = 10
        self.current_delay = 0

    def handle_input(self, keys, screen_width, screen_height):
        # Gérer les entrées du joueur (déplacement)
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        # Ajoutez la logique pour tirer avec un délai
        if keys[pygame.K_SPACE]:
            # print(keys[pygame.K_SPACE])
            if self.current_delay <= 0:
                self.fire_bullet()
                print("Tir !")
                self.current_delay = self.fire_delay  # Réinitialisez le délai

        # Mettez à jour le délai entre les tirs
        if self.current_delay > 0:
            self.current_delay -= 1

        # Vérifier si le joueur dépasse les limites de l'écran
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width

    def fire_bullet(self):
        # Créer une nouvelle instance de balle et l'ajouter à la liste des balles
        # Passer la position de départ de la balle
        bullet = Bullet(self.rect.centerx, self.rect.top)
        self.bullets.add(bullet)

    def update(self, screen_width, enemies):
        # Assurez-vous que le joueur reste à l'intérieur de l'écran
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width

        # Mettre à jour les balles du joueur
        self.bullets.update()

        # Gestion des collisions entre balles du joueur et ennemis
        self.collisions = pygame.sprite.groupcollide(
            self.bullets, enemies, True, True)

        for enemy in self.enemies_hit:
            print(f"Ennemi touché !")
            enemy.kill()

    def draw(self, screen):
        # Afficher le vaisseau spatial du joueur
        screen.blit(self.image, self.rect)

        # Afficher les balles
        self.bullets.draw(screen)
