from World import World
from Body import Body
from Bird import Bird
from geometry import Vector2D, Point2D

class Herder(Bird):


    HERD_RADIUS = 30



    def __init__(self, position, velocity, flock, world):
        Body.__init__(self, position, velocity, world)
        self.flock = flock
        self.rightmost = None
        self.velocity = velocity
        self.leave_trail = False
        self.worried = False
        self.leave_trail2 = False





    def steer(self):

        nearby = self.flock.allWithinDistance(self.HERD_RADIUS, self.position, excluding=[self])

        if nearby == None:
            return Vector2D(0.0, 0.0)
        else:
            for bird in nearby:
                if self.rightmost == None:
                    self.rightmost = bird
                heading = (bird.position - self.position).direction()
                dotP = self.velocity.dot(heading)
                if dotP < 0.0:
                    continue
                if self.rightmost == None:
                    self.rightmost = bird
                rightmostDir = (self.rightmost.position - self.position).direction()
                crossP = heading.cross(rightmostDir)
                if crossP > 0.0:
                    self.rightmost = bird
            return 1.5 * (self.rightmost.position - self.position)


    def color(self):
        return "#BCFD16"

