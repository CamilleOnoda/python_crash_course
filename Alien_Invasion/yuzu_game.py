import sys
import pygame
from girl import Girl
from settings import Settings


class YuzuGame:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()

        # Control the frame rate
        self.clock = pygame.time.Clock()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Yuzuki's game")

        # Create a girl instance after the screen has been created
        self.girl = Girl(self)


    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.clock.tick(60)
            self._update_screen()


    def _check_events(self):
            """Helper method to manage events"""
            # Watch for keyboard and mouse movement
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    
    def _update_screen(self):
         """Update images on the screen, and flip to the new screen"""
         # Redraw the screen during each pass through the loop
         self.screen.fill(self.settings.bg_color)
         # Draw the girl on the screen
         self.girl.blitme()
        # Make the most recently drawn screen visible
         pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance, and run the game.
    ai = YuzuGame()
    ai.run_game()
