# Imports
import pygame as pg  # Import the Pygame library as 'pg' for handling graphics and events
from ..window import Window  # Import the 'Window' class from another module (presumably to interact with a window)

class Image:
    """An Image to put on the display with an optional outline"""

    def __init__(self, master):
        """Constructor to initialize the image object with a master object."""
        self.master = master  # The 'master' is the main window or the object controlling this image
        self.initialize_variables()  # Call a method to set default values for image properties
        self.functions()  # Call a method to perform some setup actions (e.g., adding this image to the master window)

    def tick(self, screen):
        """Called every frame to update the image's appearance on the screen."""

        # Adjust the size of the image by subtracting the outline width to account for the outline
        self.adjusted_size = (self.size[0] - (self.outline_width * 2), self.size[1] - (self.outline_width * 2))

        # Create a transparent surface for the final image
        self.surface = pg.Surface(self.adjusted_size, pg.SRCALPHA)

        # If an outline is enabled (outline width > 0), draw the outline first
        if self.outline_width > 0:
            # Create a surface for the outline
            outline_surface = pg.Surface(self.adjusted_size, pg.SRCALPHA)
            
            # Draw the outline on the outline surface
            outline_rect = pg.Rect(0, 0, self.adjusted_size[0], self.adjusted_size[1])
            pg.draw.rect(outline_surface, self.outline_color, outline_rect, self.outline_width, border_radius=self.roundness)
            outline_surface.set_alpha(self.outline_opacity)  # Set the outline's transparency

            # Blit (copy) the outline surface onto the main surface (the final image surface)
            self.surface.blit(outline_surface, (0, 0))  # Place the outline on top of the image

        # Load the image from the specified file path
        image = pg.image.load(self.image_path)

        # Scale the image to the adjusted size
        image = pg.transform.scale(image, self.adjusted_size)

        # Rotate the image by the specified angle (if any)
        image = pg.transform.rotate(image, self.angel)

        # Apply a blur effect to the image if requested (using Gaussian blur)
        if self.blur > 0:
            image = pg.transform.gaussian_blur(image, self.blur)

        # Set the image opacity (transparency)
        image.set_alpha(self.opacity)

        # Blit (copy) the transformed image onto the surface (it will be on top of the outline)
        self.surface.blit(image, (0, 0))

        # Optionally, show other shapes if self.show is True
        if self.show:
            for shape in self.shapes:
                shape.tick(self.surface)  # Call the 'tick' method for any additional shapes

        # Finally, blit the final surface (the image with the outline and transformations) to the screen at the defined position
        screen.blit(self.surface, self.position)

    def functions(self):
        """Performs some setup functions, like adding this image to the master object (likely the window)."""
        self.master.shapes.append(self)  # Add this image to the list of shapes in the master window

    def initialize_variables(self):
        """Defines and initializes variables for the image's properties with default values."""
        self.size = (50, 50)  # Default size of the image (width, height)
        self.position = (0, 0)  # Default position of the image on the screen (x, y)
        self.event_catchers = []  # List of functions to handle events (like mouse clicks)
        self.angel = 0  # Default rotation angle for the image (0 means no rotation)
        self.show = True  # Flag that determines whether to display other shapes on top of the image
        self.opacity = 255  # Default opacity for the image (255 means fully opaque)
        self.shapes = []  # List of other shapes that can be drawn on top of the image
        self.image_path = ""  # Path to the image file (default is an empty string, meaning no image loaded)
        self.blur = 0  # Amount of blur applied to the image (default is no blur)
        self.outline_width = 0  # Default outline width (0 means no outline)
        self.outline_color = "red"  # Default outline color (red)
        self.outline_opacity = 255  # Default opacity for the outline (255 means fully opaque)
        self.roundness = 0  # Corner roundness for the outline (optional, default is sharp corners)

    def event_catcher(self, event):
        """Handles events like mouse clicks and passes them to registered event handlers."""
        for event_catcher in self.event_catchers:
            event_catcher(event)  # Call each event catcher with the event
