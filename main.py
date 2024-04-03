import pygame
import sys
from pygame.sprite import Group
from modules.game import Game
from modules.player import Player
from modules.bullet import Bullet
from modules.enemy import Enemy

# Initialisation de Pygame
pygame.init()

# Création de la fenêtre du jeu
screen_width = 1080
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jeu de Tir Spatial")

# Charger l'image de l'arrière-plan
background_image = pygame.image.load("assets/back.jpg")

# Création des objets de jeu
game = Game(screen_width, screen_height)

player = Player(screen_width, screen_height)
bullets = Group()  # Groupe pour stocker les balles
enemies = Group()  # Groupe pour stocker les ennemis
enemies_killed = 0

# Création d'une police et d'un texte pour afficher le nombre d'ennemis tués
font = pygame.font.Font(None, 36)

# Définition du délai entre chaque apparition d'ennemi (2 secondes)
enemy_spawn_delay = 1000  # en millisecondes (1 seconde)
last_enemy_spawn_time = 0

# Création de l'objet Clock pour gérer la fréquence de rafraîchissement
clock = pygame.time.Clock()

# Fonction pour afficher la modal au début du jeu


def show_modal():
    modal_text = [
        "Appuyez sur les flèches gauche/droite pour déplacer le vaisseau.",
        "Appuyez sur la barre d'espace pour tirer.",
        "Cliquez sur n'importe quelle touche pour commencer."
    ]
    modal_font = pygame.font.Font(None, 36)
    modal_rect = pygame.Rect(240, 180, 300, 300)
    pygame.draw.rect(screen, (0, 0, 0), modal_rect)  # Fond de la modal
    for i, line in enumerate(modal_text):
        text_surface = modal_font.render(line, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (screen_width // 2, 240 + i * 40)
        screen.blit(text_surface, text_rect)
    pygame.display.flip()
    waiting_for_key = True
    while waiting_for_key:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting_for_key = False


# Afficher la modal au début du jeu
show_modal()

# Boucle de jeu principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Vérifiez si suffisamment de temps s'est écoulé depuis le dernier ennemi
    current_time = pygame.time.get_ticks()
    if current_time - last_enemy_spawn_time >= enemy_spawn_delay:
        # Créez un nouvel ennemi
        enemy = Enemy(screen_width, screen_height)
        # Ajoutez l'ennemi au groupe d'ennemis
        enemies.add(enemy)
        # Mettez à jour le dernier temps d'apparition d'ennemi
        last_enemy_spawn_time = current_time

    # Gestion des entrées du joueur
    keys = pygame.key.get_pressed()
    player.handle_input(keys, screen_width, screen_height)

    # Mise à jour des objets de jeu
    player.update(screen_width, enemies)
    bullets.update()
    enemies.update()

    # Gestion des collisions entre balles et ennemis
    game.check_collisions(player, enemies, bullets)

    for enemy_list in player.collisions.values():
        for enemy in enemy_list:
            print("Ennemi touché !")
            enemy.kill()

    # Incrémentation du nombre d'ennemis tués après avoir géré les collisions
    enemies_killed += len(player.collisions)

    # Appel de la méthode check_collisions de l'objet game
    game.check_collisions(player, enemies, bullets)

    for bullets_hit, enemies_hit in player.collisions.items():
        for enemy in enemies_hit:
            enemies.remove(enemy)
            # Supprimer l'ennemi du groupe d'ennemis
            enemies.remove(enemy)

    # Afficher l'arrière-plan
    screen.blit(background_image, (0, 0))

    # Gestion de l'affichage des objets de jeu
    player.draw(screen)
    bullets.draw(screen)
    enemies.draw(screen)

    text = font.render(
        f"Ennemis tués : {enemies_killed}", True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.topleft = (10, 10)
    screen.blit(text, text_rect)

    # Rafraîchissement de l'écran
    pygame.display.flip()

    # Limitation de la fréquence de rafraîchissement
    # Réglez le nombre de FPS cible (60 FPS dans cet exemple)
    clock.tick(60)
