from vpython import *
G=6.67e-11
dt=10

scene.caption = 'Earth and Apollo 13'
scene.width = 800
scene.height = 600

earth= sphere(pos=vector(0,0,0), color=color.green)
earth.mass=5.97e24  #mass of the earth
earth.p = vector(0,0,0)*earth.mass
earth.radius = 6378.5e3  #radius of the earth

apollo=sphere(pos=vector(6378.5e3 + 173000,0,0), radius = 100e3,color=color.red)
apollo.mass = 31.3e3 #mass of apollocraft
apollo.p=vector(0,173,0)*apollo.mass
apollo.radius= 100e3
apollo.orbit=curve(pos=[apollo.pos],color=apollo.color,radius = 1e4)

while (1==1):
    rate(1000)
    # Calculating the change in p of apollo
    dist = apollo.pos - earth.pos
    force = 6.67e-11 * apollo.mass * earth.mass * dist / mag(dist)**3
    apollo.p = apollo.p - force*dt
