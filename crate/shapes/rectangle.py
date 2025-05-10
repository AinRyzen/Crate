import pygame as pg
from ..window import Window

class Rectangle:
    """A Rectangle to put on the display with an optional outline"""
    def __init__(self, master):
        self.master = master
        self.initialize_variables()
        self.functions()

    def tick(self, screen):
        """Every frame of the application you get a signal and the root"""

        # Create the surface for the rectangle
        self.surface_inner = pg.Surface(self.size, pg.SRCALPHA)

        if self.outline_width == 0:
            # No outline, just the filled rectangle
            pg.draw.rect(
                self.surface_inner,
                self.color,
                self.surface_inner.get_rect(),
                border_radius=self.roundness
            )

        else:
            # Create the outer surface to only show the outline
            self.surface_outer = pg.Surface(self.size, pg.SRCALPHA)

            # Draw the outer rectangle for the outline
            pg.draw.rect(
                self.surface_outer,
                self.outline_color,
                self.surface_outer.get_rect(),
                self.outline_width,
                border_radius=self.roundness
            )

            # Apply opacity to the outline surface
            self.surface_outer.set_alpha(self.outline_opacity)

            # Draw the inner filled rectangle (shrink it by outline width)
            inner_rect = self.surface_inner.get_rect().inflate(-self.outline_width * 2, -self.outline_width * 2)
            pg.draw.rect(
                self.surface_inner,
                self.color,
                inner_rect,
                border_radius=max(self.roundness - self.outline_width, 0)
            )

        # Apply opacity to the inner rectangle (fill)
        self.surface_inner.set_alpha(self.opacity)

        # Rotate the surfaces if needed
        if self.outline_width > 0:
            self.surface_outer = pg.transform.rotate(self.surface_outer, self.angel)
        self.surface_inner = pg.transform.rotate(self.surface_inner, self.angel)

        # Create a final surface to hold both inner and outer rectangles
        self.surface = pg.Surface(self.size, pg.SRCALPHA)

        # Blit the outer surface (outline) first if there is an outline
        if self.outline_width > 0:
            self.surface.blit(self.surface_outer, (0, 0))

        # Then, blit the inner filled rectangle (no additional offset here)
        self.surface.blit(self.surface_inner, (0, 0))  # No offset, placed directly over the outline

        # Optionally, show other shapes if self.show is True
        if self.show:
            for shape in self.shapes:
                shape.tick(self.surface)

        # Finally, blit to the screen
        screen.blit(self.surface, self.position)

    def functions(self):
        """Runs Standalone Functions"""
        self.master.shapes.append(self)

    def initialize_variables(self):
        """Defines Variables"""
        self.size = (50, 50)  # Default size
        self.position = (0, 0)
        self.event_catchers = []
        self.color = (110, 110, 110)
        self.angel = 0
        self.show = True
        self.opacity = 255
        self.shapes = []
        self.outline_width = 0
        self.outline_color = "red"
        self.outline_opacity = 255
        self.roundness = 0  # Optional corner rounding

    def event_catcher(self, event):
        """Every time an event is triggered it gets redirected here"""
        for event_catcher in self.event_catchers:
            event_catcher(event)
