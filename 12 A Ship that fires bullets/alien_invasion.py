#First, we import the sys and pygame modules
#The pygame module contains the functionality we need to make a game. 
#We’ll use tools in the sys module to exit the game when the player quits.
import sys
import pygame

from settings import Settings
from ship import Ship
# Alien Invasion starts as a class called AlienInvasion. 
class AlienInvasion:
    """Overall class to manage game assets and behavior"""
    def __init__(self):
        """Initailize the game, and create game resources"""
        # In the __init__() method, the pygame.init() function initializes the background settings that Pygame needs to work properly 1
        pygame.init()
        
        #After initializing pygame, we create an instance of the class Clock, from the pygame.time module.
        self.clock = pygame.time.Clock()
        #Then we call pygame.display.set_mode() to create a display window 2, on which we’ll draw all the game’s graphical elements. 
        self.screen=pygame.display.set_mode((1200,800))
        #The argument (1200, 800) is a tuple that defines the dimensions of the game window, which will be 1,200 pixels wide by 800 pixels high. 
        # The object we assigned to self.screen is called a surface. A surface in Pygame is a part of the screen where a game element can be displayed. Each element in the game, like an alien or a ship, is its own surface.
        
        #The surface returned by display.set_mode() represents the entire game window. When we activate the game’s animation loop, this surface will be redrawn on every pass through the loop, so it can be updated with any changes triggered by user input.
        
        self.settings=Settings()
        #We import Settings into the main program file. Then we create an instance of Settings and assign it to self.settings 1, after making the call to pygame.init().
        
        
        # When we create a screen 2, we use the screen_width and screen_height attributes of self.settings, and then we use self.settings to access the background color when filling the screen 3 as well.
        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        
        #We assign this display window to the attribute self.screen, so it will be available in all methods in the class.
        pygame.display.set_caption("Alien Invasion")
        
        #We import Ship and then make an instance of Ship after the screen has been created 1. The call to Ship() requires one argument: an instance  of AlienInvasion. The self argument here refers to the current instance of  AlienInvasion. This is the parameter that gives Ship access to the game’s resources, such as the screen object. We assign this Ship instance to self.ship.
        self.ship=Ship(self)
        
        # Set the background color.
        self.bg_color = (230, 230, 230)
        
    #The game is controlled by the run_game() method
    def run_game(self):
        """start the main loop for the game."""
        #This method contains a while loop 3 that runs continually. The while loop contains an event loop and code that manages screen updates. An event is an action that the user performs while playing the game, such as pressing a key or moving the mouse. To make our program respond to events, we write an event loop to listen for events and perform appropriate tasks depending on the kinds of events that occur. 
        while True:
             
            #The for loop 4 nested inside the while loop is an event loop.
            #Watch for keyword and mouse events.
            
            # To call a method from within a class, use dot notation with the variable self and the name of the method 1. We call the method from inside the while loop in run_game().
            self._check_events()
            
            self._update_screen()
            
            # We make a new _check_events() method 2 and move the lines that check whether the player has clicked to close the window into this new method.
    def _check_events(self):
                
                # To access the events that Pygame detects, we’ll use the pygame.event.get() function.
                #This function returns a list of events that have taken place since the last time this function was called. Any keyboard or mouse event will cause this for loop to run. Inside the loop, we’ll write a series of if statements to detect and respond to specific events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            #QUIT event is detected and we call sys.exit() to exit the game 5.        
    def _update_screen(self):
        """Updare images on the screen, and flip to the new section"""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
            
            # After filling the background, we draw the ship on the screen by calling ship.blitme(), so the ship appears on top of the background 2.
        self.ship.blitme()
            
            #Make the most recently drawn screen visible.
        pygame.display.flip()
            #The call to pygame.display.flip() 6 tells Pygame to make the most recently drawn screen visible.
            # In this case, it simply draws an empty screen on each pass through the while loop, erasing the old screen so only the new screen is visible.
            
            #When we move the game elements around, pygame.display.flip() continually updates the display to show the new positions of game elements and hide the old ones, creating the illusion of smooth movement.
            
            #The tick() method takes one argument: the frame rate for the game. Here I’m using a value of 60, so Pygame will do its best to make the loop run exactly 60 times per second.
        self.clock.tick(60)
if __name__ == '__main__':
    #make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
# At the end of the file, we create an instance of the game and then call run_game(). We place run_game() in an if block that only runs if the file is called directly. When you run this alien_invasion.py file, you should see an empty Pygame window.              
  
  
class Settings:
    "A class to store all settings for Alien Invasion." 
    
    def __init__(self):
        """initializa the game's settings"""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)      