from vpython import *

g = 9.8
k = 150000
L = 5
theta = -pi/4
scene = canvas(width=800,height=500,center=vec(0,0,0),align='left',background=vec(0.5,0.5,0))
floor = box(length=70,height=0.01,width=10,color=color.blue)
cart = box(pos=vec(-30,1.5,0),length=5,height=3,width=3,color=vec(0.5,0.5,0.5))
cart.m = 0.5
cart.v = vec(0,0,0)
cart.a = vec(0,0,0)
rod = cylinder(pos=cart.pos+vec(0,0,1.5+0.05),radius=0.05)
rod.axis = vec(L*sin(theta),L*cos(theta),0)
pendulum = sphere(radius=0.1,pos=rod.pos+rod.axis)
pendulum.m = 0.2
pendulum.v = vec(0,0,0)
pendulum.a = vec(0,0,0)

dt=0.001
while True:
    rate(1000)
    T = -k*(rod.axis.mag-L) * rod.axis.norm()
    cart.a.x = -T.x/cart.m
    pendulum.a = vec(0,-g,0) + T/pendulum.m
    cart.v += cart.a * dt
    pendulum.v += pendulum.a * dt
    cart.pos += cart.v * dt
    pendulum.pos += pendulum.v * dt
    rod.pos = cart.pos+vec(0,0,1.5+0.05)
    rod.axis = pendulum.pos - rod.pos
