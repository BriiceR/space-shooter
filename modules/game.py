import pygame


class Game:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

    def check_collisions(self, player, enemies, bullets):
        # Vérification de la collision entre le joueur et les ennemis
        player_hit = pygame.sprite.spritecollide(player, enemies, True)
        if player_hit:
            # Gérer la collision ici (par exemple, diminuer la vie du joueur)
            print("player_hit")
            pass

        # Vérification de la collision entre les balles et les ennemis
        bullets_hit = player.collisions
        if bullets_hit:
            print("bullets_hit")
            pass

    # Ajoutez d'autres méthodes de gestion des collisions au besoin

    # Vous pouvez également ajouter d'autres méthodes de gestion du jeu ici
