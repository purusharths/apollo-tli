from vpython import *
import time
scene.width = 1600
scene.height = 900
moon = sphere(pos=vector(6,0,0), radius=0.1, make_trail=True)
moon.trail_color = color.green
moon.texture = {'file':textures.rough, 'bumpmap':None}

earth = sphere(radius=0.7)
earth.texture = {'file':textures.earth, 'bumpmap':None}
earth.rotate(angle=5, axis=vector(0,0,0))
t=27
moon.rotate(angle=5.14,
           axis=moon.pos,
           origin=earth.pos)

while True:
    rate(9)
    earth.rotate(angle=23.4, axis=earth.pos+vector(0,1,0))
    moon.rotate(angle=5.16, axis=moon.pos+vector(0,1,0))

"""
r = moon.pos
while r.x<10:
	rate(10)
	moon.pos = vector(r.x*cos(2*pi*t), r.y*sin(2*pi*t), 0)
	print(moon.pos)
	r.x = r.x + 1
	r.y = r.y + 1
"""
