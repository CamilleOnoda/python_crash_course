import pygame


class Girl:
    """A class to manage the girl"""

    def __init__(self, ai_game):
        """Initialize the girl and set its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the girl image and get its rect
        self.image = pygame.image.load("images/girl_hat_pink.bmp")
        self.rect = self.image.get_rect()

        # Start each new girl at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom


    def blitme(self):
        """ Draw the girl at its current location"""
        self.screen.blit(self.image, self.rect)