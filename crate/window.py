# Imports
import pygame as pg  # Import the Pygame library as 'pg' for handling graphics and events
from typing import List  # Import 'List' to specify that some variables will hold lists of objects
import ctypes  # Import ctypes to interact with system-level functions (used for window positioning)

from .shapes.shape import Shape  # Import the 'Shape' class (presumably a custom class for shapes)

class Window:
    """A class to create and manage a graphical window."""
    
    def __init__(self, title_bar=True, size=(500, 500)):
        """Constructor that sets up the window with a title bar and size."""
        self.title_bar = title_bar  # Boolean flag to decide if the window should have a title bar
        self.size = size  # The dimensions of the window (width, height)
        
        self.initialize_variables()  # Call the method to initialize all the necessary variables
        self.functions()  # Call the method to perform some initial setup functions (like setting title)

    def initialize_variables(self): 
        """Sets up the window's variables with default values."""
        
        # Cosmetic settings (visual appearance)
        self.color = "green"  # Background color of the window (green)
        self.position = (ctypes.windll.user32.GetSystemMetrics(0) // 2 - self.size[0] // 2,
                         ctypes.windll.user32.GetSystemMetrics(1) // 2 - self.size[1] // 2) 
        # Set the initial position of the window to be centered on the screen
        self.title = "Crate Window"  # Window title displayed in the title bar
        self.closeable = True  # Whether the window can be closed (via the 'X' button)
        self.fps = 120  # Frames per second (the speed at which the window updates)
        self.allow_screensaver = True  # Whether screensaver is allowed while the window is open
        self.window_icon = None  # Icon for the window (None means no icon)

        # Important settings (control window behavior)
        self.running = True  # This flag controls whether the window is still open or not
        self.shapes: List[Shape] = []  # List of 'Shape' objects that will be drawn in the window
        self.ticks = []  # List of functions to be executed each frame (tick)
        self.event_catchers = []  # List of event handler functions for catching events (like mouse clicks)

        # Internal setup (Pygame-specific)
        if self.title_bar:
            self.screen = pg.display.set_mode(self.size)  # Create the window with a title bar
        else:
            self.screen = pg.display.set_mode(self.size, pg.NOFRAME)  # Create the window without a title bar
        self._ignore_next_move_event = False  # Flag to prevent reacting to window move events triggered by our code
        self._should_update_window_position = False  # Flag to indicate if we need to move the window

        self.clock = pg.time.Clock()  # Create a clock to manage the FPS
        self.hwnd = pg.display.get_wm_info()['window']  # Get the window handle (for low-level system calls)

    def loop(self):
        """Starts the main loop that keeps the window running."""
        
        while self.running:  # This loop keeps the window open as long as 'running' is True
            self.screen.fill(self.color)  # Fill the screen with the background color (green)

            # Process events (like button clicks, key presses, etc.)
            for event in pg.event.get():
                if event.type == pg.QUIT and self.closeable:
                    # If the window is closeable and the user clicked the 'X', close the window
                    self.running = False
                    
                if event.type == pg.WINDOWMOVED:
                    if self._ignore_next_move_event:
                        # If this move was triggered by our code, don't update the position
                        self._ignore_next_move_event = False
                    else:
                        # If the user moved the window, update the position
                        new_pos = (event.dict["x"], event.dict["y"])
                        if new_pos != self.position:  # If the new position is different from the old one
                            self.position = new_pos
                    
                for shape in self.shapes:
                    # Pass the event to each shape to handle (for things like mouse clicks on shapes)
                    shape.event_catcher(event)

            # Update all the shapes on the screen
            for shape in self.shapes:
                shape.tick(self.screen)  # Call the 'tick' method to update the shape

            # Call all functions in 'ticks' (e.g., actions that need to happen every frame)
            for tick in self.ticks:
                tick()

            pg.display.flip()  # Update the display to show all the drawn content

            self.reconfigure_window()  # Update the window's position and size if needed
            
            self.clock.tick(self.fps)  # Limit the FPS to the specified value

    def reconfigure_window(self):
        """Handles repositioning the window if a manual move has been requested."""
        if self._should_update_window_position:
            self._ignore_next_move_event = True  # Ignore any move events triggered by our own move command
            ctypes.windll.user32.MoveWindow(self.hwnd, self.position[0], self.position[1], self.size[0], self.size[1], True)
            self._should_update_window_position = False  # Reset flag to avoid constant moving

    def centre_window(self):
        """Centers the window on the screen."""
        self.position = (
            ctypes.windll.user32.GetSystemMetrics(0) // 2 - self.size[0] // 2,  # Calculate center position (x)
            ctypes.windll.user32.GetSystemMetrics(1) // 2 - self.size[1] // 2   # Calculate center position (y)
        )
        self._should_update_window_position = True  # Set the flag to move the window to the new position

    def functions(self):
        """Performs some setup actions for the window."""
        
        pg.display.set_caption(self.title)  # Set the title of the window
        pg.display.set_allow_screensaver(self.allow_screensaver)  # Allow or disallow screensavers
        if self.window_icon is not None:
            pg.display.set_icon(self.window_icon)  # Set the window icon (if provided)
