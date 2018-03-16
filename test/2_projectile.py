from vpython import *
import time

#def projectile(v0, theta, mass):

"""
Makes the projectile motion based on the inputs.
v0: Initial Velocity
theta: angle
ball.mass: mass of the ball
"""
mass = 0.5 #float(input("Mass: "))
v0 = 4.0 #float(input("Initial Velocity: "))
theta = 45 #float(input("Angle: "))
#projectile(v0, theta, mass)

floor = box(pos=vector(0,-.02,0), size=vector(2,0.02,0.4))
ball = sphere(pos=vector(-1,0,0),radius=0.02, color=color.red, make_trail=True)
g = vector(0,-9.8,0)

ball.mass = mass
ball.p = vector(v0*cos(theta), v0*sin(theta),0) * ball.mass
t=0
dt = 0.01

while ball.pos.y >= 0:
    if not t: # rate too fast for geko engine.
        time.sleep(2) # confusing. Use time lib instead
    rate(80)
    Fnet = ball.mass * g
    ball.p =  ball.p + Fnet * dt
    ball.pos = ball.pos + ball.p*dt / ball.mass
    t = t + dt

if __name__ == "__main__":
    pass
