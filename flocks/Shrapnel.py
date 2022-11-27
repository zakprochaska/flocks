from Body import Body
from ShrapnelTrail import ShrapnelTrail
from geometry import Vector2D, Point2D


class Shrapnel(Body):



    FIREWORK_RADIUS = 15
    
    def __init__(self, position, velocity, world, firework):
        self.position = position
        self.velocity = velocity
        self.world = world
        self.firework = firework
        self.age = 0
        self.accel = Vector2D()


    def steer(self):
        dist = (self.firework.position-self.position).magnitude()
        if dist < self.FIREWORK_RADIUS:
            return Vector2D(0.0, 0.0)
        else:
            return Vector2D(0.0, -0.1)

    
    def step(self):
        self.age += 1
        Body.step(self)
        shrapTrail = ShrapnelTrail(self, self.world)
        self.world.addBody(shrapTrail)
        if self.age > 30:
            self.world.removeBody(self)

    def color(self):
        if self.firework.colorInt == 0:
            if self.age < 5:
                return "#FFFFFF"
            elif self.age < 10:
                return "#FFFF00"
            elif self.age < 20:
                return "#FF4C00"
            else:
                return "#A3A3A3"
        elif self.firework.colorInt == 1:
            if self.age < 5:
                return "#FFFFFF"
            elif self.age < 10:
                return "#0AB1F7"
            elif self.age < 20:
                return "#0AF745"
            else:
                return "#A3A3A3"
        elif self.firework.colorInt == 2:
            if self.age < 5:
                return "#FFFFFF"
            elif self.age < 10:
                return "#9A0AF7"
            elif self.age < 20:
                return "#F70ACE"
            else:
                return "#A3A3A3"