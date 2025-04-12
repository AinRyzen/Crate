# Imports

import pygame as pg
from typing import List

from .shapes.shape import Shape

class Window:
    
    """Creates a crate window"""
    
    def __init__(self):
        
        self.initialize_variables()
        
        self.functions()
        
    def initialize_variables(self): 
        """ Sets Variables """
        
        # Cosmetic
        self.color = "green" # Background Color
        self.size = (500,500) # Window size
        self.title = "Crate Window" # Window title
        self.closeable = True # Decide if window is closeable
        self.fps = 120 # At witch fps is the window looked
        self.allow_screensaver = True # Decides if screensaver can be active while the window is open
        self.window_icon = None
        self.title_bar = True
        
        # Important
        self.running = True # As long as this is true the window continues to run
        self.shapes : List[Shape] = [] # A list of Classes called shapes
        self.ticks = [] # A list of function that are executed every tick
        self.event_catchers = [] # A list of functions that get executed when a event is caught
        
        # Internal
        self.previous_title_bar = True
        self.screen = pg.display.set_mode(self.size) # Create the screen
        self.clock = pg.time.Clock() # Create a clock to later look the fps
         
    def loop(self): # Run by the user
        """Starts the window loop"""
        
        while self.running:
            
            self.screen.fill(self.color) 
            # Constantly overwrite the screen with your color
            
            if not pg.display.get_window_size() == self.size:
                self.screen = pg.display.set_mode(self.size)

            if not self.title_bar == self.previous_title_bar:
                if self.title_bar is False:

                    if self.title_bar is False:
                        self.screen = pg.display.set_mode(self.size,pg.NOFRAME)
                        self.previous_title_bar = self.title_bar

                    elif self.title_bar is True:
                        self.screen = pg.display.set_mode(self.size)
                        self.previous_title_bar = self.title_bar

            # Updates the window size
            
            for event in pg.event.get():
                # Listens to events like "Right mouse button was clicked"
                if event.type == pg.QUIT and self.closeable:
                    # Closes the window if X clicked
                    self.running = False

                    
                for shape in self.shapes:
                    # passes the event to the shapes
                    shape.event_catcher(event)
                    
            for shape in self.shapes:
                # Updates the shapes
                shape.tick(self.screen)

            for tick in self.ticks:
                tick()
                
            pg.display.flip()
            # updates the screen to show all the drawn content
            
            self.clock.tick(self.fps)
            # limits FPS to self.fps
                      
    def functions(self):
        """Runs Standalone functions"""
        
        pg.display.set_caption(self.title)
        # Sets the window title
        
        pg.display.set_allow_screensaver(self.allow_screensaver)
        # Decides if screensaver can be active while the window is open
        
        if self.window_icon is not None : pg.display.set_icon(self.window_icon)
        # Add a window icon
    
    