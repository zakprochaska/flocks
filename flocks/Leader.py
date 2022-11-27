from World import World
from Body import Body
from Bird import Bird
from geometry import Vector2D

class Leader(Bird):
    

    def steer(self):

        FOLLOW_RADIUS = 10

        mousePos = self.world.pointer()
        mouseVec = mousePos - self.position
        distance = mouseVec.magnitude()

        if distance > FOLLOW_RADIUS:
            return mouseVec
        else:
            return Vector2D(0.0, 0.0)


    def color(self):
        return "#FFFF00"

    