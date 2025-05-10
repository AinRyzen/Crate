# Import the Pygame library for handling graphics and events
import pygame as pg  
from ..window import Window  # Import the Window class to interact with the main window

class Line:
    """A Line to put on the display (can be drawn with configurable properties such as size, color, and opacity)"""
    
    def __init__(self, master):
        """Constructor to initialize the line object with a master object (the window or container)."""
        self.master = master  # The 'master' is the main window or object that manages this line
        self.initialize_variables()  # Initialize the line with default values
        self.functions()  # Perform setup actions like adding the line to the master window

    def tick(self, screen):
        """Called every frame to update and render the line on the screen."""
        
        # Create a transparent surface that is large enough to hold the line
        self.surface = pg.Surface((self.end_position[0] + self.start_position[0], self.end_position[1] + self.start_position[1]), pg.SRCALPHA)
        
        # Draw the line on the surface using the given color, start and end positions, and line thickness
        pg.draw.line(self.surface, self.color, self.start_position, self.end_position, self.size)
        
        # Rotate the surface (line) if an angle is specified
        self.surface = pg.transform.rotate(self.surface, self.angel)

        # Set the opacity of the surface (line) based on the opacity variable
        self.surface.set_alpha(self.opacity)

        # Optionally, show other shapes if self.show is True
        if self.show:
            for shape in self.shapes:
                shape.tick(self.surface)  # Call the 'tick' method for any additional shapes

            # Blit (copy) the rendered line onto the screen at the defined start position
            screen.blit(self.surface, self.start_position)

    def functions(self):
        """Performs some setup functions like adding this line to the master window's shapes list."""
        self.master.shapes.append(self)  # Add this line to the list of shapes in the master window

    def initialize_variables(self):
        """Defines and initializes variables for the line's properties with default values."""
        self.size = 10  # Default thickness of the line
        self.start_position = (0, 0)  # Start position (x, y) of the line
        self.end_position = (5, 5)  # End position (x, y) of the line
        self.color = (110, 110, 110)  # Default color of the line (gray)
        self.event_catchers = []  # List of functions to handle events (like mouse clicks)
        self.angel = 0  # Default rotation angle for the line (0 means no rotation)
        self.show = True  # Flag that determines whether to display other shapes on top of the line
        self.opacity = 255  # Default opacity for the line (255 means fully opaque)
        self.shapes = []  # List of other shapes that can be drawn on top of the line

    def event_catcher(self, event):
        """Handles events like mouse clicks and passes them to registered event handlers."""
        for event_catcher in self.event_catchers:
            event_catcher(event)  # Call each event catcher with the event
