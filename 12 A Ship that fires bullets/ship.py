import pygame

class Ship:
    """A class to manage the ship"""
    
    def __init__(self,ai_game):
        """Initialize the ship and set its starting position"""
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()
        
        # Load the ship image and get its rect.
        # To load the image, we call pygame.image.load() 3 and give it the location of our ship image. 
        #This function returns a surface representing the ship, which we assign to self.image. When the image is loaded, we call get_rect() to access the ship surface’s rect attribute so we can later use it to place the ship.
        self.image = pygame.image.load('image1.jpeg')
        # When the image is loaded, we call get_rect() to access the ship surface’s rect attribute so we can later use it to place the ship.
        self.rect = self.image.get_rect()
        # When the image is loaded, we call get_rect() to access the ship surface’s rect attribute so we can later use it to place the ship.
        
        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        # We’ll position the ship at the bottom center of the screen. To do so, make the value of self.rect.midbottom match the midbottom attribute of the screen’s rect 4. Pygame uses these rect attributes to position the ship image so it’s centered horizontally and aligned with the bottom of the screen.
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)