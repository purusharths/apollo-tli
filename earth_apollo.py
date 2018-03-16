from vpython import *

#universal variables
G = 6.67e-11 #Universal Gravitational Constant
dt = 10 #rate of change of time

scene = display(tite='Earth and apollo 13', width=800, height=600)

#earth
earth = sphere(pos=(0,0,0), color=color.green)
earth.mass = 5.97e24
earth.p = vector(0,0,0) * earth.mass
earth.radius = 6378.5e3

#apollo
moon = sphere(pos=(0,0,0), color=color.green)
moon.mass = 5.97e24
moon.p = vector(0,0,0) * moon.mass
moon.radius = 6378.5e3


