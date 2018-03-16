from vpython import *
from math import *
import os
import subprocess
import time

G=6.67e-11
dt= 25 # Step Wise
 
scene.width = 1366
scene.height = 768
scene.center = vector(250e6,0,0)
 
 
# Parking Orbit (Earth)
T = 5040
# Time init sec
t = 0
# Translunar Injection Angle
TLI_theta = pi
# Translunar Injection Angle Init
theta = 0
# Earth Variables
earth= sphere(pos=vector(0,0,0), color=color.blue)
earth.velocity = vector(0,0,0)
earth.mass=5.97e24
earth.radius = 6378.5e3
 
# Apollo Variables
apollo=sphere(pos=vector(6551e3,0,0),color=color.green,make_trail=True, trail_type='points', interval=10, retain=50)
apollo.velocity=vector(0,7792,0)
apollo.radius= 100e3
 
# Moon Variables
d =36.6*0.0174533
a = ((sin(d))*384.4e6)
b = ((cos(d))*384.4e6)
c = ((sin(d))*1022)
e = ((cos(d))*1022)
moon=sphere(pos=vector(a,-b,0),color=color.white)
moon.velocity=vector(e,c,0)
moon.mass=7.3480e22
moon.radius=2.238e6
 
# Moon and Apollo Trail Curve
apollo.trail=curve(pos=[apollo.pos],color=color.green)
moon.trail=curve(pos=[moon.pos],color=color.white)
 
TLI = True
 
def acceleration(ob1, ob2):
    rVector = ob1.pos-ob2.pos
    acc = -((G * ob2.mass) / rVector.mag2 ) * rVector.norm()
    return(acc)
 
while (t<3800000):
    time.sleep(0.001)
    rate(1000)
    # Time iteration every 10 sec
    t = t+dt
    # TLI angle update
    theta = (2*pi*t)/T
 
    # Prograde Burn toward Moon
    if( (theta > TLI_theta) & TLI):
        TLI = False
        TLI_velocity = 10943.5
        R_parking = 6551e3
 
        apollo.velocity = TLI_velocity*vector(-sin(TLI_theta),cos(TLI_theta),0)
        apollo.pos      = R_parking*vector(cos(TLI_theta), sin(TLI_theta), 0)
        #apollo.velocity = vector(0, -TLI_velocity, 0)
 
    # Apollo Acceleration
    apollo.acceleration = acceleration(apollo, earth) + acceleration(apollo, moon)
 
    # Apollo State Vector
    apollo.velocity=apollo.velocity+apollo.acceleration*dt
    apollo.pos=apollo.pos+apollo.velocity*dt
    apollo.trail.append(pos=apollo.pos)
 
    # Moon Acceleration
    moon.acceleration = acceleration(moon, earth)
 
    # Moon State Vector
    moon.velocity=moon.velocity+moon.acceleration*dt
    moon.pos=moon.pos+moon.velocity*dt
    moon.trail.append(pos=moon.pos)
    print("\tMoon: {}\tApollo: {}".format(moon.pos, apollo.pos))
