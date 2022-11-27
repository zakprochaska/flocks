from World import World
from Body import Body
from Bird import Bird
from Mouse import Mouse

class Chaser(Bird):

    def computeCohere(self):

        mousePos = self.world.pointer()
        selfPos = self.position
        direcV = mousePos - selfPos

        return direcV.direction()
        