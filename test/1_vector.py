from vpython import *

ball1 = sphere(pos=vector(0,0,0), radius=0.1,  color=color.red)
ball2 = sphere(pos=vector(-2,-1,0), radius=0.1,  color=color.green)
ball3 = sphere(pos=vector(1,-1.5,0), radius=0.1,  color=color.yellow)

print(ball1.pos)
rtemp = 2*ball1.pos
print(rtemp)
A = vector(2,-3,-1)
print(rtemp+A)


"""
For the arrow object, there are two important attributes.  “pos” is the
location of the start of the arrow and “axis” is a vector from the
starting position to the end of the arrow

for each arrow pos will be the starting point. and axis will be the mag/di5r 
"""

vec_arrow12 = arrow(pos=ball1.pos, axis=ball2.pos, color=color.blue)
vec_arrow13 = arrow(pos=ball1.pos, axis=ball3.pos, color=color.yellow)
vec_arrow32 = arrow(pos=ball2.pos, axis=vector(ball3.pos.x-ball2.pos.x, ball3.pos.y-ball2.pos.y, ball3.pos.z-ball2.pos.z), color=color.white)
