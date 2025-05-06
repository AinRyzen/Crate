# Imports

import pygame as pg
from typing import List
import ctypes

from .shapes.shape import Shape

class Window:
    
    """Creates a crate window"""
    
    def __init__(self,title_bar=True,size=(500,500)):
        self.title_bar = title_bar
        self.size = size
        
        self.initialize_variables()
        
        self.functions()
        
    def initialize_variables(self): 
        """ Sets Variables """
        
        # Cosmetic
        self.color = "green" # Background Color
        self.position = (ctypes.windll.user32.GetSystemMetrics(0) // 2 - self.size[0] // 2, ctypes.windll.user32.GetSystemMetrics(1) // 2 - self.size[1] // 2)
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
        self._ignore_next_move_event = False # Prevents reacting to our own MoveWindow() call in the next frame
        self._should_update_window_position = False # Tells the system to update the window's position in the next frame
        
        self.clock = pg.time.Clock() # Create a clock to later look the fps
        self.hwnd = pg.display.get_wm_info()['window'] # Gets the window
         
    def loop(self): # Run by the user
        """Starts the window loop"""
        
        while self.running:
            
            self.screen.fill(self.color)
            # Constantly overwrite the screen with your color

            # Updates the window size
            
            for event in pg.event.get():
                # Listens to events like "Right mouse button was clicked"
                if event.type == pg.QUIT and self.closeable:
                    # Closes the window if X clicked
                    self.running = False
                    
                if event.type == pg.WINDOWMOVED:
                    if self._ignore_next_move_event:
                        # This move was triggered by us, not the user — ignore it
                        self._ignore_next_move_event = False
                    else:
                        # User moved the window — update our internal position
                        new_pos = (event.dict["x"], event.dict["y"])
                        if new_pos != self.position:
                            self.position = new_pos
                    
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
            
            self.reconfigure_window()
            # updates the window size and position constantly
            
            self.clock.tick(self.fps)
            # limits FPS to self.fps
            
    def reconfigure_window(self):
        """Moves the window only when a manual position update was requested"""
        if self._should_update_window_position:
            self._ignore_next_move_event = True  # Set to ignore the WINDOWMOVED event triggered by this
            ctypes.windll.user32.MoveWindow(
                self.hwnd,
                self.position[0],
                self.position[1],
                self.size[0],
                self.size[1],
                True
            )
            self._should_update_window_position = False  # Reset so it doesn't keep moving


    def centre_window(self):
        """Centers the window on the screen and schedules a one-time move"""
        self.position = (
            ctypes.windll.user32.GetSystemMetrics(0) // 2 - self.size[0] // 2,
            ctypes.windll.user32.GetSystemMetrics(1) // 2 - self.size[1] // 2
        )
        self._should_update_window_position = True  # Request window movement


            
    def functions(self):
        """Runs Standalone functions"""
        
        pg.display.set_caption(self.title)
        # Sets the window title
        
        pg.display.set_allow_screensaver(self.allow_screensaver)
        # Decides if screensaver can be active while the window is open
        
        if self.window_icon is not None : pg.display.set_icon(self.window_icon)
        # Add a window icon
    
    