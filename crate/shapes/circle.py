import pygame as pg
from ..window import Window

class Circle:
    """A Circle to put on the display"""
    def __init__(self, master):
        self.master = master
        
        self.initialize_variables()
        self.functions()
        
    def tick(self, screen):
        """Every frame of the application you get a signal and the root"""

        self.adjusted_size = self.size-(self.outline_width*2)
        # Create the surface for the circle with transparency (SRCALPHA)
        self.surface = pg.Surface((self.adjusted_size, self.adjusted_size), pg.SRCALPHA)

        if self.outline_width == 0:
            # No outline, just the filled circle
            pg.draw.circle(self.surface, self.color, (self.adjusted_size // 2, self.adjusted_size // 2), self.adjusted_size // 2)
        
        elif self.outline_width > 0:
            # Create the outer surface for the outline and apply the outline's opacity
            self.surface_outer = pg.Surface((self.adjusted_size, self.adjusted_size), pg.SRCALPHA)
            pg.draw.circle(self.surface_outer, self.outline_color, (self.adjusted_size // 2, self.adjusted_size // 2), self.adjusted_size // 2)
            
            # Use a smaller circle to "erase" the center of the outer circle, leaving just the outline
            inner_radius = self.adjusted_size // 2 - self.outline_width
            pg.draw.circle(self.surface_outer, (0, 0, 0, 0), (self.adjusted_size // 2, self.adjusted_size // 2), inner_radius)

            # Set opacity for the outline
            self.surface_outer.set_alpha(self.outline_opacity)

            # Blit the outline surface onto the main surface
            self.surface.blit(self.surface_outer, (0, 0))

            # Draw the inner filled circle smaller to make room for the outline
            pg.draw.circle(self.surface, self.color, (self.adjusted_size // 2, self.adjusted_size // 2), self.adjusted_size // 2 - self.outline_width)

        # Apply opacity to the entire surface (will affect both outline and fill)
        self.surface.set_alpha(self.opacity)

        # Optionally, show other shapes if self.show is True
        if self.show:
            for shape in self.shapes:
                shape.tick(self.surface)
            
            # Blit the final surface to the screen at the defined position
            screen.blit(self.surface, self.position)
            

    def functions(self):
        """Runs Standalone Functions"""
        self.master.shapes.append(self)

    def initialize_variables(self):
        """Defines Variables"""
        self.position = (0, 0)
        self.color = (110, 110, 110)  # Default fill color
        self.event_catchers = []
        self.size = 50  # Default size
        self.show = True
        self.opacity = 255  # Default opacity for the inner circle
        self.shapes = []
        self.outline_width = 0  # Default outline width
        self.outline_color = "red"  # Default outline color
        self.outline_opacity = 255  # Default opacity for the outline
        
    def event_catcher(self, event):
        """Every time an event is triggered it gets redirected here"""
        for event_catcher in self.event_catchers:
            event_catcher(event)
