from Body import Body
from World import World
from geometry import Vector2D, Point2D


class ShrapnelTrail(Body):


    def __init__(self, shrapnel, world):
        self.velocity = Vector2D()
        self.position = shrapnel.position
        self.shrapnel = shrapnel
        self.world = world
        Body.__init__(self, shrapnel.position, self.velocity, self.world)
        self.age = 0

    def steer(self):
        return Vector2D()


    def color(self):
        return self.shrapnel.color()

    
    def step(self):
        self.age += 1
        Body.step(self)
        if self.age > 10:
            self.world.removeBody(self)
