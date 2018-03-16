from vpython import *

def proj(v0,theta):
    #this function takes a ball at x=0,y=0 and launches it
    #theta is in radians
    ball=sphere(pos=vector(0,0,0),radius=0.02, make_trail=True)
    ball.m=0.1
    ball.p=vector(v0*cos(theta), v0*sin(theta),0)*ball.m
    g=vector(0,-9.8,0)
    t=0
    dt=0.01
                
    while ball.pos.y>=0:
        Fnet=ball.m*g
        ball.p=ball.p+Fnet*dt
        ball.pos=ball.pos+ball.p*dt/ball.m
        t=t+dt
                  
proj(4,45*pi/180)
proj(4,90*pi/180)
proj(4,35*pi/180)
proj(4,40*pi/180)
proj(40, 60*pi/180)

