# Imports
import pygame as pg  # Import the Pygame library as 'pg' for handling graphics and events
from ..window import Window  # Import the 'Window' class from another module (presumably to interact with a window)

class Rectangle:
    """A Rectangle to put on the display with an optional outline"""

    def __init__(self, master):
        """Constructor for initializing the rectangle object with a master object."""
        self.master = master  # The 'master' is the main window or the object controlling this rectangle
        self.initialize_variables()  # Call a method to set default values for rectangle properties
        self.functions()  # Call a method to perform some setup actions (e.g., adding this rectangle to the master window)

    def tick(self, screen):
        """The main method called every frame to update the rectangle's appearance on the screen."""

        # Create a transparent surface for the inner part of the rectangle (without the outline)
        self.surface_inner = pg.Surface(self.size, pg.SRCALPHA)

        if self.outline_width == 0:
            # If no outline is set (outline width is 0), draw a solid filled rectangle
            pg.draw.rect(
                self.surface_inner,  # The surface to draw on (the inner rectangle)
                self.color,  # The fill color of the rectangle
                self.surface_inner.get_rect(),  # The rectangle area to fill (takes the surface size)
                border_radius=self.roundness  # Optional rounded corners (set to 0 for square corners)
            )
        else:
            # If an outline is specified, we need to draw the outer rectangle first (outline)
            self.surface_outer = pg.Surface(self.size, pg.SRCALPHA)

            # Draw the outer rectangle (outline) with specified width and color
            pg.draw.rect(
                self.surface_outer,  # The surface to draw on (the outer rectangle)
                self.outline_color,  # Color of the outline
                self.surface_outer.get_rect(),  # The rectangle area to draw the outline in
                self.outline_width,  # Width of the outline
                border_radius=self.roundness  # Optional rounded corners for the outline
            )

            # Apply the opacity to the outline surface (controls the transparency of the outline)
            self.surface_outer.set_alpha(self.outline_opacity)

            # Now, create the inner filled rectangle by shrinking the rectangle size by the outline width
            inner_rect = self.surface_inner.get_rect().inflate(-self.outline_width * 2, -self.outline_width * 2)
            # Draw the inner rectangle (filled) inside the outline
            pg.draw.rect(
                self.surface_inner,  # The surface to draw on (the inner rectangle)
                self.color,  # The fill color for the inner rectangle
                inner_rect,  # The shrunk inner rectangle (to leave space for the outline)
                border_radius=max(self.roundness - self.outline_width, 0)  # Reduce roundness if outline exists
            )

        # Apply opacity to the inner rectangle (controls transparency of the fill)
        self.surface_inner.set_alpha(self.opacity)

        # Rotate the surfaces if needed (rotation angle is given by self.angle)
        if self.outline_width > 0:
            self.surface_outer = pg.transform.rotate(self.surface_outer, self.angle)  # Rotate the outline
        self.surface_inner = pg.transform.rotate(self.surface_inner, self.angle)  # Rotate the inner rectangle

        # Create a final surface to combine both the inner and outer rectangles
        self.surface = pg.Surface(self.size, pg.SRCALPHA)

        # Blit the outer surface (outline) first if there's an outline
        if self.outline_width > 0:
            self.surface.blit(self.surface_outer, (0, 0))

        # Then, blit the inner filled rectangle (no additional offset, placed directly over the outline)
        self.surface.blit(self.surface_inner, (0, 0))

        # Optionally, show other shapes if self.show is True (if there are other shapes to draw on top)
        if self.show:
            for shape in self.shapes:
                shape.tick(self.surface)  # Call 'tick' method of other shapes to update them

        # Finally, blit the final rectangle to the screen at the specified position
        screen.blit(self.surface, self.position)

    def functions(self):
        """Performs some setup functions, like adding this rectangle to the master object (likely the window)."""
        self.master.shapes.append(self)  # Add this rectangle to the list of shapes in the master window

    def initialize_variables(self):
        """Defines and initializes variables for the rectangle's properties with default values."""
        self.size = (50, 50)  # Default size of the rectangle (width, height)
        self.position = (0, 0)  # Default position of the rectangle on the screen (x, y)
        self.event_catchers = []  # List of functions to handle events (like mouse clicks)
        self.color = (110, 110, 110)  # Default fill color for the rectangle (a shade of gray)
        self.angle = 0  # Default rotation angle for the rectangle (0 means no rotation)
        self.show = True  # Flag that determines whether to display other shapes on top of the rectangle
        self.opacity = 255  # Default opacity for the rectangle (255 means fully opaque)
        self.shapes = []  # List of other shapes that can be drawn on top of the rectangle
        self.outline_width = 0  # Default outline width (0 means no outline)
        self.outline_color = "red"  # Default color of the outline (red)
        self.outline_opacity = 255  # Default opacity of the outline (255 means fully opaque)
        self.roundness = 0  # Default corner roundness (0 means sharp corners)

    def event_catcher(self, event):
        """Handles events like mouse clicks and passes them to the registered event handlers."""
        for event_catcher in self.event_catchers:
            event_catcher(event)  # Call each event catcher with the event
