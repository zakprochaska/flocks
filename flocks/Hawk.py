from World import World
from Body import Body
from Bird import Bird
from geometry import Vector2D, Point2D

class Hawk(Bird):

    def __init__(self, position, velocity, flock, world):
        Body.__init__(self, position, velocity, world)
        self.flock = flock

    

    def computeCohere(self):

        nearby = self.flock.allWithinDistance(1000.0, self.position, excluding=[self])

        # Try to be around other birds.
        cohere  = Vector2D()
        for other in nearby:
            offset = other.position - self.position
            cohere = cohere + offset

        # We'll normalize the cohere vector.  If we don't, birds will
        # work harder if they are further away from the center of the
        # group.  That's a nice effect, too, but it often creates
        # instabilities in the activity of the simulation.
        return cohere.direction()

    def steer(self):

        return self.computeCohere()


    def step(self):
        Body.step(self)


    def color(self):
        return "#FF0000"

        