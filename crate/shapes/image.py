import pygame as pg
from ..window import Window

class Image:
    """An Image to put on the display with an optional outline"""
    def __init__(self, master):
        self.master = master
        self.initialize_variables()
        self.functions()

    def tick(self, screen):
        """Every frame of the application you get a signal and the root"""

        
        self.adjusted_size = (self.size[0]-(self.outline_width*2),self.size[1]-(self.outline_width*2))
        # Create the surface for the final image with transparency
        self.surface = pg.Surface(self.adjusted_size, pg.SRCALPHA)

        # If the outline is enabled
        if self.outline_width > 0:
            # Create surface for the outline
            outline_surface = pg.Surface(self.adjusted_size, pg.SRCALPHA)
            
            # Draw the outline on the outline surface
            outline_rect = pg.Rect(0, 0, self.adjusted_size[0], self.adjusted_size[1])
            pg.draw.rect(outline_surface, self.outline_color, outline_rect, self.outline_width, border_radius=self.roundness)
            outline_surface.set_alpha(self.outline_opacity)  # Set the outline opacity

            # Blit the outline surface onto the main surface
            self.surface.blit(outline_surface, (0, 0))  # Outline will be on top

        # Load and transform the image
        image = pg.image.load(self.image_path)
        image = pg.transform.scale(image, self.adjusted_size)
        image = pg.transform.rotate(image, self.angel)

        # Apply blur to the image if requested (Gaussian blur)
        if self.blur > 0:
            image = pg.transform.gaussian_blur(image, self.blur)

        image.set_alpha(self.opacity)  # Set the image opacity

        # Blit the image onto the surface (it will be on top of the outline)
        self.surface.blit(image, (0, 0))

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
        self.size = (50, 50)  # Default size
        self.position = (0, 0)
        self.event_catchers = []
        self.angel = 0
        self.show = True
        self.opacity = 255  # Default opacity for the image
        self.shapes = []
        self.image_path = ""  # Path to the image file
        self.blur = 0  # Amount of blur applied to the image
        self.outline_width = 0  # Default outline width (0 means no outline)
        self.outline_color = "red"  # Default outline color (red)
        self.outline_opacity = 255  # Default opacity for the outline
        self.roundness = 0  # Corner roundness for the outline (optional)

    def event_catcher(self, event):
        """Every time an event is triggered it gets redirected here"""
        for event_catcher in self.event_catchers:
            event_catcher(event)
