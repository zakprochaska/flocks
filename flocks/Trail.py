from Body import Body
from geometry import *

class Trail(Body):

    def __init__(self, bird):
        self.velocity = -1.0 * bird.velocity + Vector2D.random(0.3)
        Body.__init__(self, bird.position, self.velocity, bird.world)

    def step(self):

        Body.step(self)
        if self.velocity.magnitude() < 0.05:
            self.world.removeBody(self)
        

    def color(self):
        if self.velocity.magnitude() > 1:
            return "#FFFFFF"
        elif self.velocity.magnitude() > 0.5:
            return "#FFDF00"
        elif self.velocity.magnitude() > 0.25:
            return "#FF4C00"
        else:
            return "#A99086"


    def steer(self):
        return -0.3 * self.velocity