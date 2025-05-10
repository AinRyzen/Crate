import pygame as pg  # Importing the Pygame library as 'pg' for drawing and handling graphics
from ..window import Window  # Importing the 'Window' class from a parent directory (managing the game window)

class Circle:
    """A Circle to put on the display"""

    def __init__(self, master):
        """Constructor that sets up the initial state of the circle."""
        self.master = master  # 'master' is the object that owns or manages this circle (could be a container)
        
        self.initialize_variables()  # Initialize the variables (position, color, size, etc.)
        self.functions()  # Add this circle to the list of shapes managed by the master

    def tick(self, screen):
        """Update the circle every frame and draw it on the screen."""
        
        # Adjust the circle size to account for the outline width
        self.adjusted_size = self.size - (self.outline_width * 2)
        
        # Create a surface (empty image) with transparency to draw the circle
        self.surface = pg.Surface((self.adjusted_size, self.adjusted_size), pg.SRCALPHA)
        
        # If there is no outline, just draw a filled circle
        if self.outline_width == 0:
            pg.draw.circle(self.surface, self.color, (self.adjusted_size // 2, self.adjusted_size // 2), self.adjusted_size // 2)
        
        # If there is an outline, draw the circle with an outline
        elif self.outline_width > 0:
            # Create another surface for the outline (transparent)
            self.surface_outer = pg.Surface((self.adjusted_size, self.adjusted_size), pg.SRCALPHA)
            
            # Draw the outer circle (outline) on the surface
            pg.draw.circle(self.surface_outer, self.outline_color, (self.adjusted_size // 2, self.adjusted_size // 2), self.adjusted_size // 2)
            
            # Calculate the radius of the inner circle that will be "erased" from the outline
            inner_radius = self.adjusted_size // 2 - self.outline_width
            pg.draw.circle(self.surface_outer, (0, 0, 0, 0), (self.adjusted_size // 2, self.adjusted_size // 2), inner_radius)

            # Set the transparency (opacity) of the outline
            self.surface_outer.set_alpha(self.outline_opacity)

            # Draw the outline surface on top of the main surface
            self.surface.blit(self.surface_outer, (0, 0))

            # Draw the inner filled circle (smaller to leave space for the outline)
            pg.draw.circle(self.surface, self.color, (self.adjusted_size // 2, self.adjusted_size // 2), self.adjusted_size // 2 - self.outline_width)

        # Apply transparency (opacity) to the whole circle, including the outline and fill
        self.surface.set_alpha(self.opacity)

        # If the circle is set to show additional shapes, draw them as well
        if self.show:
            for shape in self.shapes:
                shape.tick(self.surface)
        
        # Draw the circle on the screen at the specified position
        screen.blit(self.surface, self.position)

    def functions(self):
        """Registers the circle in the master list of shapes."""
        self.master.shapes.append(self)  # Add this circle to the 'shapes' list of the master object

    def initialize_variables(self):
        """Sets up the default variables for the circle."""
        self.position = (0, 0)  # Position where the circle will appear on the screen (x, y)
        self.color = (110, 110, 110)  # Default fill color of the circle (gray)
        self.event_catchers = []  # List to store event handlers (functions that react to events)
        self.size = 50  # Default size of the circle (diameter)
        self.show = True  # Boolean that controls whether the circle should be shown or not
        self.opacity = 255  # Default opacity (255 means fully opaque)
        self.shapes = []  # List to store other shapes associated with this circle
        self.outline_width = 0  # Default outline width (0 means no outline)
        self.outline_color = "red"  # Default color of the outline (red)
        self.outline_opacity = 255  # Default opacity of the outline

    def event_catcher(self, event):
        """Handles events triggered by the system, like clicks or key presses."""
        for event_catcher in self.event_catchers:
            event_catcher(event)  # Call each event handler in the 'event_catchers' list with the event as argument
