import sys

import pygame

def check_events():
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
            
def update_screen(mount_settings, screen, mountain):
    """Update images on the screen adn flip to the new screen."""
    screen.fill(mount_settings.bg_color)
    mountain.blitme()
    
    pygame.display.flip()