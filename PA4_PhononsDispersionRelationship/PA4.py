import numpy as np
from vpython import *

#constants/variables
A, N, omega = 0.10, 50, 2*pi/1.0
#amplitude, num of ball, angular frequency
size, m, k, d = 0.06, 0.1, 10.0, 0.4
# ball size, ball mass, stiffness constant, distance between 2 balls
Unit_K, n = 2 * pi/(N*d), 1
#initialize n(number of wave)
dt = 0.0003

#background setup & graphing
#scene = canvas(title='Spring Wave', width=800, height=300,\
        #background=vec(0.5,0.5,0), center = vec((N-1)*d/2, 0, 0))
relation = graph(title='Dispersion Relationship',width = 800, align = 'left', \
                 xtitle='wave vector',ytitle='angular frequency',background=vec(0.5,0.5,0))
x = gcurve(color=color.red,graph = relation)

#Objects setup
'''
balls = [sphere(radius=size, color=color.red, pos=vector(i*d, 0, 0), v=vector(0,0,0)) for i in range(N)] #3
springs = [helix(radius = size/2.0, thickness = d/15.0, pos=vector(i*d, 0, 0), axis=vector(d,0,0)) for i in range(N-1)] #3
c = curve([vector(i*d, 1.0, 0) for i in range(N)], color=color.black) #visualize the waves
'''
#n-changing loop
for n in range(1,int(N/2)):
    T=0
    Wavevector = n * Unit_K
    phase = Wavevector * arange(N) * d
    ball_pos, ball_orig = np.arange(N)*d + A*np.sin(phase),np.arange(N)*d
    ball_v, spring_len =  np.zeros(N), np.ones(N)*d
    Next=True
    #Motion start
    while True:
        #rate(1000)
        spring_len[:-1] =ball_pos[1:]-ball_pos[:-1]
        ball_v[1:] += dt*k*(spring_len[1:]-spring_len[:-1])/m
        spring_len[N-1]=ball_pos[0]+50*d-ball_pos[N-1]
        ball_pos[N-1]+= dt*k*(spring_len[N-1]-spring_len[-1])/m
        #6
        ball_v[0]=dt*k*(spring_len[0]-spring_len[N-1])/m
        ball_pos += ball_v*dt
        ball_disp = ball_pos - ball_orig
        '''
        #change the position of each object
        for i in range(N):
            balls[i].pos.x = ball_pos[i] #3
        for i in range(N-1): #3
            springs[i].pos = balls[i].pos #3
            springs[i].axis = balls[i+1].pos - balls[i].pos #3   
        for i in range(N):
            c.modify(i, y = ball_disp[i]*4+1)
        '''
        #start the period accumulation
        if ball_v[1]<0:
            T+=dt
            Next=False
        #to the Next n
        if ball_v[1]>0 and Next==False:
            omega=pi/T
            x.plot(pos=(Wavevector,omega))
            break
        
