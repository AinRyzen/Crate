# Imports

import pygame as pg
from typing import List
import ctypes

from .shapes.shape import Shape

class Window:
    
    """Creates a crate window"""
    
    def __init__(self,title_bar):
        self.title_bar = title_bar
        
        self.initialize_variables()
        
        self.functions()
        
    def initialize_variables(self): 
        """ Sets Variables """
        
        # Cosmetic
        self.color = "green" # Background Color
        self.size = (500,500) # Window size
        self.position = (100,100)
        self.title = "Crate Window" # Window title
        self.closeable = True # Decide if window is closeable
        self.fps = 120 # At witch fps is the window looked
        self.allow_screensaver = True # Decides if screensaver can be active while the window is open
        self.window_icon = None
        
        # Important
        self.running = True # As long as this is true the window continues to run
        self.shapes : List[Shape] = [] # A list of Classes called shapes
        self.ticks = [] # A list of function that are executed every tick
        self.event_catchers = [] # A list of functions that get executed when a event is caught
        
        # Internal
        if self.title_bar:self.screen = pg.display.set_mode(self.size) # Create the screen
        else: self.screen = pg.display.set_mode(self.size,pg.NOFRAME) # Create the screen#
        
        self.clock = pg.time.Clock() # Create a clock to later look the fps
        self.hwnd = pg.display.get_wm_info()['window'] # Gets the window
         
    def loop(self): # Run by the user
        """Starts the window loop"""
        
        while self.running:
            
            self.screen.fill(self.color) 
            # Constantly overwrite the screen with your color
            
            if not pg.display.get_window_size() == self.size:
                self.reconfigure_window()

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
            
    def reconfigure_window(self):
        """Moves The window"""
        ctypes.windll.user32.MoveWindow(self.hwnd, self.position[0], self.position[1], self.size[0],self.size[1], True)
                      
    def functions(self):
        """Runs Standalone functions"""
        
        pg.display.set_caption(self.title)
        # Sets the window title
        
        pg.display.set_allow_screensaver(self.allow_screensaver)
        # Decides if screensaver can be active while the window is open
        
        if self.window_icon is not None : pg.display.set_icon(self.window_icon)
        # Add a window icon
    
    