from vpython import *

# constants setup and variables
g=9.8 
size = 0.25  # ball radius = 0.25 m
theta = pi/4
C_drag = 0.9
vi = 20 
height=15.0
t=0
final_pos=vec(0,0,0)
counter=0
total_dis=0

# building environment
scene = canvas(width=800, height=800, center =vec(0,height/2,0), background=vec(0.5,0.5,0)) 
floor = box(length=30, height=0.01, width=10, color=color.blue) # the floor
ball = sphere(radius = size, color=color.red, make_trail = True, trail_radius = 0.05) # the ball
initial_pos=vec( -15, size, 0) # ball initial position
ball.pos =initial_pos
ball.v = vec(vi*cos(theta), vi*sin(theta), 0) # ball initial velocity
l_height=0 #largest height
dt = 0.001 # time step

# graphing
arr1=arrow(color=color.green,shafwidth=0.05)
osillisation= graph(width=450,align='right'+'top')
f1=gcurve(graph=osillisation,color=color.green,width=3)

# start motion
while counter<3: # bounce back for 3 times
    rate(1000) 
    t+=dt
    ball.pos += ball.v*dt
    ball.v += vec(0,-g,0)*dt-C_drag*ball.v*dt

    # arrow
    arr1.pos = ball.pos
    arr1.axis = vec(ball.v)*0.2
    # v-t graphing
    v_mag=ball.v.mag
    f1.plot(pos = (t,v_mag))
    if ball.pos.y<=size and ball.v.y<0: #bounce back (change the direction)
        ball.v.y=-ball.v.y
        counter+=1
    if ball.pos.y>l_height: # update the largest height
        l_height= ball.pos.y
    total_dis+=(ball.v*dt).mag #sum the total distance
final_pos=ball.pos
displacement=final_pos-initial_pos # displacement

#text output
msg =text(text = 'Displacement='+str(displacement.mag),pos = vec(-10, 8, 0))
msg =text(text = 'Total Distance='+str(total_dis),pos = vec(-10, 10, 0))
msg =text(text = 'Largest Height='+str(l_height), pos = vec(-10, 12, 0))

''' 
problem1 : error showing the graph: 'invalid syntax'
solution:f1.plot '='<--- should not appear (pos = (t,v_mag))
'''
    


