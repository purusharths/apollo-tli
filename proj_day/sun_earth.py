from vpython import *
import time

earth = sphere(pos=vector(0,0,0), radius=60)
earth.texture = {'file':textures.earth}
earth.mass = 5.9e25

moon = sphere(pos=vector(-200,0,0), radius=10, make_trail=True)
moon.trail_color = color.green
#moon.trail_type='points'
moon.texture = {'file':textures.rough, 'bumpmap':None}

#moon.rotate(angle=5.14, axis=moon.pos, origin=earth.pos)
moon.mass = 7.3e22
moon.v = vector(0,-9,0)

Gr= 6.6e-11
t = 0
dt = 0.01

while True:
        if not t:
            time.sleep(4)
        rate(100) #refresh rate
        #rotation
        earth.rotate(angle=23.4, axis=earth.pos+vector(0,0.1,0))
        moon.rotate(angle=5.16, axis=moon.pos+vector(0,1,0))
        #revolution
        dist = (moon.pos.x**2 + moon.pos.y**2)**0.5
        radialVector = (earth.pos - moon.pos)/dist
        Fgrav = 10000*radialVector/dist**2
        #Fgrav =  Gr* (moon.mass * earth.mass)/(dist**2)
        moon.v += Fgrav
        moon.pos += moon.v
        t = t + dt
        #if dist<= earth.radius:
        #       break
