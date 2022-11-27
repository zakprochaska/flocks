from Body import Body
from geometry import *

class Trail2(Body):

    def __init__(self, bird):
        self.velocity = Vector2D()
        Body.__init__(self, bird.position, self.velocity, bird.world)
        self.age = 0

    def step(self):
        Body.step(self)
        self.age += 1
        if self.age > 18:
            self.world.removeBody(self)

    def color(self):
        if self.age < 3:
            return "#DA0C0C"
        elif self.age < 6:
            return "#FF8000"
        elif self.age < 9:
            return "#FFFF00"
        elif self.age < 12:
            return "#00FF00"
        elif self.age < 15:
            return "#0000FF"
        else:
            return "#A802FF"

    def steer(self):
        return Vector2D()