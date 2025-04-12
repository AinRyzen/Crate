import pygame as pg
from ..window import Window

class Image:
    """A Image to put on the display"""
    def __init__(self,master):

        self.master = master
        
        self.initialize_variables()
        self.functions()
        
    def tick(self,screen):
        """Every frame of the application you get a signal and the root"""

        self.surface = pg.image.load(self.image_path)
        
        self.surface = pg.transform.scale(self.surface,self.size)
        self.surface = pg.transform.rotate(self.surface,self.angel)
        if self.blur > 0:
            self.surface = pg.transform.gaussian_blur(self.surface,self.blur)
        self.surface.set_alpha(self.opacity)
 
        if self.show:
            for shape in self.shapes:
                shape.tick(self.surface)
            screen.blit(self.surface, self.position)
            

    
    def functions(self):
        """Runs Standalone Functions"""

        self.master.shapes.append(self)

         
    def initialize_variables(self):
        """Defines Variables"""

        self.size = (50,50)
        self.position = (0, 0)
        self.event_catchers = []
        self.angel = 0
        self.show = True
        self.opacity = 255
        self.shapes = []
        self.image_path = ""
        self.blur = 0 
        
    def event_catcher(self,event):
        """Every time an event is triggered it gets redirected here"""

        for event_catcher in self.event_catchers:
            event_catcher(event)
        