import pygame
import pygame_gui


class InstructionModal:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.manager = pygame_gui.UIManager(
            (self.screen_width, self.screen_height))

        # Créez une fenêtre de modal
        self.modal_window = pygame_gui.elements.UIWindow(
            pygame.Rect(self.screen_width // 4, self.screen_height //
                        4, self.screen_width // 2, self.screen_height // 2),
            self.manager,
            "Instructions",
            pygame_gui.windows.UIMessageWindow
        )

        # Ajoutez du texte d'instructions
        self.instructions = pygame_gui.elements.UITextBox(
            "Appuyez sur les flèches gauche/droite pour déplacer le vaisseau.\nAppuyez sur la barre d'espace pour tirer.\nCliquez sur OK pour commencer.",
            pygame.Rect(20, 40, self.screen_width // 2 -
                        40, self.screen_height // 2 - 80),
            self.manager,
            self.modal_window
        )

        # Ajoutez un bouton OK
        self.ok_button = pygame_gui.elements.UIButton(
            pygame.Rect(self.screen_width // 2 - 60,
                        self.screen_height // 2 - 40, 120, 30),
            "OK",
            self.manager,
            self.modal_window
        )

    def run(self, screen):
        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.ok_button:
                            running = False

                self.manager.process_events(event)

            self.manager.update(clock.tick(60) / 1000.0)
            screen.fill((0, 0, 0))

            self.manager.draw_ui(screen)
            pygame.display.flip()

        pygame.quit()
