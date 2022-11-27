from World import World
from Body import Body
from Bird import Bird
from Leader import Leader
from geometry import Vector2D, Point2D

class Follower(Bird):


    def computeCohere(self):

        if self.flock.leader == None:
            nearby = self.flock.allWithinDistance(self.COHERE_RADIUS, self.position, excluding=[self])

            # Try to be around other birds.
            cohere  = Vector2D()
            for other in nearby:
                offset = other.position - self.position
                cohere = cohere + offset

            return cohere.direction()
        else:
            leaderPos = self.flock.leader.position
            return leaderPos - self.position