from World import World
from Body import Body
from Bird import Bird
from geometry import Vector2D

class Mouse(Bird):
    
    def __init__(self, world):
        self.world = world
        self.position = self.world.pointer()

    def step(self):
        self.position = self.world.pointer()
        
        
    def shape(self):
        # A little square is our generic shape.
        p1 = self.position + Vector2D( 0.125, 0.125)       
        p2 = self.position + Vector2D(-0.125, 0.125)        
        p3 = self.position + Vector2D(-0.125,-0.125)        
        p4 = self.position + Vector2D( 0.125,-0.125)
        return [p1,p2,p3,p4]
    

    def color(self):
        return "#E03AE3"
