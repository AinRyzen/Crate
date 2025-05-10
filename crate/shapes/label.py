# Imports
import pygame as pg  # Import the Pygame library as 'pg' for handling graphics and events
from ..window import Window  # Import the 'Window' class from another module (presumably to interact with a window)

class Label:
    """A Label to put on the display (like text with optional transformations)"""

    def __init__(self, master):
        """Constructor to initialize the label object with a master object (the window or container)."""
        self.master = master  # The 'master' is the main window or the object controlling this label
        self.initialize_variables()  # Initialize the label with default values
        self.functions()  # Perform setup actions like adding the label to the master window

    def tick(self, screen):
        """Called every frame to update and render the label on the screen."""

        # Create a font object using the font file path and size
        self.text_font = pg.font.Font(self.font_file_path, self.font_size)

        # Render the text onto a surface with the specified font, color, and background color
        self.surface = self.text_font.render(self.text, True, self.font_color, bgcolor=self.color)

        # Rotate the surface (text) if an angle is specified
        self.surface = pg.transform.rotate(self.surface, self.angel)

        # Apply a blur effect to the surface if blur is greater than 0
        if self.blur > 0:
            self.surface = pg.transform.gaussian_blur(self.surface, self.blur)

        # Set the opacity of the surface (text) based on the opacity variable
        self.surface.set_alpha(self.opacity)

        # Optionally, show other shapes if self.show is True
        if self.show:
            for shape in self.shapes:
                shape.tick(self.surface)  # Call the 'tick' method for any additional shapes

            # Blit (copy) the rendered text onto the screen at the defined position
            screen.blit(self.surface, self.position)

    def functions(self):
        """Performs some setup functions like adding this label to the master window's shapes list."""
        self.master.shapes.append(self)  # Add this label to the list of shapes in the master window

    def initialize_variables(self):
        """Defines and initializes variables for the label's properties with default values."""
        self.size = (50, 50)  # Default size for the label (unused directly, but might be needed for container dimensions)
        self.position = (0, 0)  # Position of the label on the screen (x, y)
        self.color = None  # Background color of the label (optional)
        self.font_color = "#ffffff"  # Default font color (white)
        self.event_catchers = []  # List of functions to handle events (like mouse clicks)
        self.angel = 0  # Default rotation angle for the label (0 means no rotation)
        self.blur = 0  # Amount of blur applied to the label (0 means no blur)
        self.show = True  # Flag that determines whether to display other shapes on top of the label
        self.opacity = 255  # Default opacity for the label (255 means fully opaque)
        self.shapes = []  # List of other shapes that can be drawn on top of the label
        self.font_size = 48  # Default font size for the label text
        self.text = "Hello Crate!"  # Default text displayed on the label
        self.font_file_path = None  # Path to the font file (None means default system font)

    def event_catcher(self, event):
        """Handles events like mouse clicks and passes them to registered event handlers."""
        for event_catcher in self.event_catchers:
            event_catcher(event)  # Call each event catcher with the event
