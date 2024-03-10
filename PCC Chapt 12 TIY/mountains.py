import pygame

class Mountain():
    
    def __init__(self, screen):
        """Initialize the mountain and set its starting position."""
        self.screen = screen
        
        # Load the mountain image and get its rect.
        self.image = pygame.image.load('images/mountainpic.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # place on the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)