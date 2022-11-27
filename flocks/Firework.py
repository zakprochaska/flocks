import time
from World import World
from Body import Body
from Shrapnel import Shrapnel
from geometry import Vector2D, Point2D
from FuseParticle import FuseParticle

class Firework(Body):

    def __init__(self, position, velocity, world, fuseLength, color):
        self.fuseLength = fuseLength
        self.fuse = True
        self.position = position
        self.world = world
        self.velocity = velocity
        self.accel = Vector2D(0.0, -0.1)
        self.colorInt = color
        
    def steer(self):
        return Vector2D(0.0, -0.5)

    def explode(self):
        north = Shrapnel(self.position, Vector2D(0.0, 2.0), self.world, self)
        northEast = Shrapnel(self.position, Vector2D(1.414, 1.414), self.world, self)
        east = Shrapnel(self.position, Vector2D(2.0, 0), self.world, self)
        southEast = Shrapnel(self.position, Vector2D(1.0, -1.0), self.world, self)
        south = Shrapnel(self.position, Vector2D(0.0, -1.0), self.world, self)
        southWest = Shrapnel(self.position, Vector2D(-1.0, -1.0), self.world, self)
        west = Shrapnel(self.position, Vector2D(-2.0, 0.0), self.world, self)
        northWest = Shrapnel(self.position, Vector2D(1.414, 1.414), self.world, self)

        self.world.addBody(north)
        self.world.addBody(northEast)
        self.world.addBody(east)
        self.world.addBody(southEast)
        self.world.addBody(south)
        self.world.addBody(southWest)
        self.world.addBody(west)
        self.world.addBody(northWest)



    def step(self):
        Body.step(self)
        self.fuseLength -= 1
        if self.fuseLength == 0:
            self.fuse = False
        if self.fuse:
            fuseP = FuseParticle(self)
            self.world.addBody(fuseP)
        else:
            self.explode()
            self.world.removeBody(self)

        

        



