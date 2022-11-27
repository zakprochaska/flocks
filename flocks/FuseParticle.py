from Body import Body
from geometry import Vector2D, Point2D


class FuseParticle(Body):

    def __init__(self, firework):
        self.velocity = -1.0 * firework.velocity + Vector2D.random(0.3)
        Body.__init__(self, firework.position, self.velocity, firework.world)

    def step(self):

        Body.step(self)
        if self.velocity.magnitude() < 0.05:
            self.world.removeBody(self)
        

    def color(self):
        if self.velocity.magnitude() > 0.5:
            return "#FFFFFF"
        else:
            return "#515151"
        

    def steer(self):
        return -0.3 * self.velocity

    
