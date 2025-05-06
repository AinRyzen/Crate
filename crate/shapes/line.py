from ..modules import pygame as pg
from ..window import Window

class Line:
    """A Line to put on the display"""
    def __init__(self,master):

        self.master = master
        
        self.initialize_variables()
        self.functions()
        
    def tick(self,screen):
        """Every frame of the application you get a signal and the root"""

        self.surface = pg.Surface((self.end_position[0]+self.start_position[0],self.end_position[1]+self.start_position[1]),pg.SRCALPHA)
        
        pg.draw.line(self.surface,self.color,self.start_position,self.end_position,self.size )

        self.surface = pg.transform.rotate(self.surface,self.angel)
        self.surface.set_alpha(self.opacity)
 
        if self.show:
            for shape in self.shapes:
                shape.tick(self.surface)
            screen.blit(self.surface, self.start_position)
            

    
    def functions(self):
        """Runs Standalone Functions"""

        self.master.shapes.append(self)

         
    def initialize_variables(self):
        """Defines Variables"""

        self.size = 10
        self.start_position = (0, 0)
        self.end_position = (5, 5)
        self.color = (110, 110, 110 )
        self.event_catchers = []
        self.angel = 0
        self.show = True
        self.opacity = 255
        self.shapes = []
        
    def event_catcher(self,event):
        """Every time an event is triggered it gets redirected here"""

        for event_catcher in self.event_catchers:
            event_catcher(event)
        