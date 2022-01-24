from vpython import *

# constants setup and variables
g=vec(0,-9.8,0)
size = 0.2 # each ball radius
mass=1 # each ball mass
t=0
N=2 #number of lifted ball
r_length,p_dis,K = 2,0.4,150000 #(length of rope ,distance between pivots, force constant)
total_K,total_P=0,0

# building environment & setup balls
scene = canvas(width=800, height=800, center =vec(0.4, 0.2,0), background=vec(0,0.5,0.5)) 
balls=[]
ropes=[]
pivots=[]
for i in range(5):
    rope=cylinder(pos=vec(i*p_dis,r_length,0),radius=0.005)
    ropes.append(rope)
    ball=sphere(pos=vec(i*p_dis,0,0),radius=size,color=color.white)
    balls.append(ball)
    pivot=sphere(pos=vec(i*p_dis,r_length,0),radius=0.05)
    pivots.append(pivot)
    # assign axis/mass/velocity
    ropes[i].axis = balls[i].pos - ropes[i].pos
    balls[i].m=mass           
    balls[i].v = vec(0, 0, 0)


#lifting the ball(s)
for i in range (N):
    balls[i].pos+=vec(-0.4444,0.05,0)
    ropes[i].axis = balls[i].pos - ropes[i].pos


# graphing setup
energy_t= graph(width=450,align='right')
potential=gcurve(graph=energy_t,color=color.blue,width=3)
kinetic=gcurve(graph=energy_t,color=color.red,width=3)

avg_t= graph(width=450,align='right')
avg_po=gcurve(graph=avg_t,color=color.blue,width=3)
avg_ki=gcurve(graph=avg_t,color=color.red,width=3)


#function of collision
def collision(m1,m2, v1,v2, x1,x2,):
    v1_prime = v1 + 2*(m2/(m1+m2))*(x1-x2) * dot (v2-v1, x1-x2) / dot (x1-x2, x1-x2)
    v2_prime = v2 + 2*(m1/(m1+m2))*(x2-x1) * dot (v1-v2, x2-x1) / dot (x2-x1, x2-x1)
    return (v1_prime, v2_prime)


dt = 0.0001 # time step
counter=0
# start motion
while True:
    rate(5000) 
    t+=dt
    counter+=1
    # changing rope:axis/tension and ball:speed/position/velocity
    for i in range(5):
        ropes[i].axis = balls[i].pos - ropes[i].pos
        rope_force = - K * (mag(ropes[i].axis) - r_length) * ropes[i].axis.norm()
        balls[i].a = g + rope_force / mass
        balls[i].v += balls[i].a*dt
        balls[i].pos += balls[i].v*dt

    #collision occurs
    for i in range(4):
        if ((balls[i].pos - balls[i+1].pos).mag <= p_dis and dot(balls[i].pos-balls[i+1].pos, balls[i].v-balls[i+1].v) <= 0):
            (balls[i].v, balls[i+1].v) = collision (balls[i].m, balls[i+1].m, balls[i].v, balls[i+1].v, balls[i].pos, balls[i+1].pos)
 

    # graphing1  potential &kinetic energy-t
    instant_ksum=0
    instant_psum=0
    for ball in balls:
        instant_ksum+=mass*(ball.v).mag*(ball.v).mag/2
        instant_psum+=(ball.pos.y*9.8*mass)

    potential.plot(pos = (t,instant_psum))
    kinetic.plot(pos=(t,instant_ksum))

    # graphing2 average
    total_P+=instant_psum
    total_K+=instant_ksum
    

    avg_po.plot(pos=(t,total_P/counter))
    avg_ki.plot(pos=(t,total_K/counter))



