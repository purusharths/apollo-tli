from vpython import *
#scene=display(title='Earth and Ranger....Ultimate Code. Version Super Hotness......Staphanie Chan, Alfonso "COOL GUY" Rueda, Jesus Godinez!',width=1024,height=768,background=(-1.50e11,0,0))
#scene.autoscale=0
#scene.range = 3.9e8

earth = sphere()
earth.pos = vector(0,0,0)
earth.radius = 6.37e6
earth.color = color.blue
earth.mass = 5.98e24
earth.velocity = vector(0,29747,0)
earth.p = earth.velocity * earth.mass
earthlabel=label(pos = earth.pos, text = 'Earth', xoffset = 10, yoffset = 10, space = earth.radius, height = 10, border = 6, color=color.blue)

moon = sphere()
moon.pos = vector(3.82e8,0,0)
moon.radius = 1.74e6
moon.color = color.white
moon.mass = 7.36e22
moon.velocity=vector(0,30769,0)
moon.p = moon.velocity*moon.mass
moonlabel=label(pos = moon.pos, text = 'Moon', xoffset = -10, yoffset = 10, space = moon.radius, height = 10, border = 6, color=color.white)

ranger=sphere(pos=(6551e3,0,0),color=color.red)
ranger.velocity=vector(0,21944,0)
ranger.radius=75e3
ranger.mass = 306.2
ranger.p=ranger.mass*ranger.velocity
ranger.trail=curve(pos=[ranger.pos],color=ranger.color)
rangerlabel=label(pos = ranger.pos, text = 'Ranger', xoffset = 50, yoffset = 50, space = ranger.radius, height = 10, border = 6, color=color.red)

sunvelocity=vector(0,0,0)
sunradius=6.96e8
sunmass = 1.99e30
sunp=sunmass*sunvelocity
sunpos=vector(-1.5e11,0,0)

for a in [earth, moon, ranger]:
    a.orbit = curve(color=a.color, radius = 1)
    a.trail = curve(pos=[a.pos], color=a.color)

dt = 1

#Time(in secs) to complete 1 revolution around the earth
T=5040
#Time(in secs) for calculating simulation time
t=0
#Angle at which Translunar Injection occurs
TLI_theta=3.43*pi
#Angle to check for Translunar Injection
theta=0

TLI=true
TLI2=true
TLI3=true

while 1:
    rate(5000)

    if t<22210:
        scene.center=earth.pos

    if t>22210:
        scene.center = moon.pos
        scene.range = 1e7
    
    t=t+dt

    theta=(2*pi*t)/T

    dist1 = moon.pos - earth.pos
    dist2 = ranger.pos - earth.pos
    dist3 = moon.pos - ranger.pos
    dist4 = moon.pos - sunpos
    dist5 = ranger.pos - sunpos
    dist6 = earth.pos - sunpos

    if mag(dist3)<(1.74e6):
        print(mag(dist3))
        ranger.color=color.orange

    if mag(dist3)<(1.76e6):
        print(mag(dist3))
        
    if t>23822:
        if mag(dist3)>(1.76e6):
            print(mag(dist3))
            ranger.color=color.green
    
    force1 = 6.7e-11 * earth.mass * moon.mass* dist1 / mag(dist1)**3
    force2 = 6.7e-11 * earth.mass * ranger.mass* dist2 / mag(dist2)**3
    force3 = 6.7e-11 * moon.mass * ranger.mass* dist3 / mag(dist3)**3
    force4 = 6.7e-11 * sunmass * moon.mass* dist4 / mag(dist4)**3
    force5 = 6.7e-11 * sunmass * ranger.mass* dist5 / mag(dist5)**3
    force6 = 6.7e-11 * sunmass * earth.mass* dist6 / mag(dist6)**3

    earth.p = earth.p + force1*dt - force6*dt
    moon.p = moon.p - force1*dt - force4*dt
    ranger.p = ranger.p - force2*dt - force5*dt + force3*dt

    if ((theta>TLI_theta) & TLI):
        TLI=false
        #print t
        #print ranger.p
        TLI_velocity=50000
        ranger.p=TLI_velocity*vector(.6,.69356,0)*ranger.mass
        #print ranger.p
        
    for a in [earth, moon, ranger,]:
        a.pos = a.pos + a.p/a.mass * dt
        a.orbit.append(pos=a.pos)
        a.trail.append(pos=a.pos)

        if ((ranger.x>moon.x+1.76e6)& TLI2):
            TLI2=false
            #print t
            #print ranger.p
            TLI2_velocity = 29098.9
            ranger.p=TLI2_velocity*vector(0.005,1,0)*ranger.mass
            #print ranger.p
            
        if (t>20000)& (ranger.y<moon.y)& TLI3:
            TLI3 = false
            #print t
            #print dist3
            #print ranger.p
            TLI3_velocity=29099.72
            ranger.p=TLI3_velocity*vector(-.0056,.9999,0)*ranger.mass
            #print ranger.p


        
            
    earthlabel.pos = earth.pos
    moonlabel.pos = moon.pos
    rangerlabel.pos = ranger.pos
    if rangerlabel.x>3.3e8:
        rangerlabel.xoffset=-50


