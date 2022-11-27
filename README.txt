Hello Grader! For my programmer's choice option I chose to create fireworks.
To do this, I created a subclass of Body called Firework, which takes a position,
a velocity, a fuseLength and a int representing color. A Firework object has constant 
downward acceleration and is given a mostly upward velocity upon initialization, 
causing it to fly up and ark down before exploding. It knows to explode because during
each iteration of the simulation, it throws behind a fuse particle, which is essentially
the same as Trail, and its fuseLength decreases by one. When its fuseLength reaches
0, it calls an explode() method. The explode() method creates 8 Shrapnel objects, which
is another subclass of Body. They have the same downward acceleration as Fireworks and each
velocity is pointing away from its Firework at one of the 8 compass directions, N, NE, etc.
These Shrapnel objects also leave behind a trail of ShrapnelTrail objects, whose color return
the same color of their shrapnel, creating the fireworks' colorful trails.

My sim7.py file is very simple: it creates a world exactly the same as in the bird simulations
and creates three fireworks with three different color schemes, then adds them all to the world
and iterates 150 steps of the simulation, as once the fireworks go off and disappear, the simulation
can end. I also had it do this whole process twice so its easier to see what's going on.
