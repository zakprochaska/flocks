import time
from World import World
from Body import Body
from Firework import Firework
from geometry import Vector2D, Point2D

i = 0
while i < 2:
    i += 1
    world = World(60.0,45.0,800,600,topology='wrapped')
    fire1 = Firework(Point2D(0.0, 0.0), Vector2D(1.0, 3.0), world, 25, 0)
    fire2 = Firework(Point2D(50, 0.0), Vector2D(-1.0, 3.5), world, 27, 1)
    fire3 = Firework(Point2D(60, 0.0), Vector2D(-0.5, 4.0), world, 30, 2)

    world.addBody(fire1)

    world.addBody(fire2)

    world.addBody(fire3)

    n = 0

    while n < 100:
        n += 1
        time.sleep(0.03)
        world.step()
        world.render()