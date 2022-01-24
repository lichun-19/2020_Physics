
from vpython import *
#constants and variables
G=6.673E-11
mass = {'earth': 5.97E24, 'moon': 7.36E22, 'sun':1.99E30}
radius = {'earth': 6.371E6*10, 'moon': 1.317E6*10, 'sun':6.95E8*10} #10 times larger for better view 
earth_orbit = {'r': 1.495E11, 'v': 2.9783E4}
moon_orbit = {'r': 3.84E8, 'v': 1.022E3}
theta = 5.145*pi/180.0
t_total=0
dt=60*60 #1 hour
start_new_cycle=False
ans=0

#background setup
scene = canvas(width=2000, height=1000, center=vec(0, 0, 0), background=vec(0,0,0))
scene.lights = [] #turn off
local_light(pos=vector(0,0,0))


#the G force
def G_force(m1,m2,pos1,pos2):
 return G * m1 * m2 / mag2(pos2-pos1) * norm(pos2-pos1)


#center of mass
center=vector(earth_orbit['r'],0,0)
x_e=moon_orbit['r']*mass['moon']/(mass['moon']+mass['earth'])
x_m=moon_orbit['r']*mass['earth']/(mass['moon']+mass['earth'])

#properties of the starssss
earth = sphere(radius = radius['earth'],pos=center+vector(-cos(theta),sin(theta),0)*x_e,texture={'file':textures.earth})
sun = sphere(pos = vector(0,0,0), radius = radius['sun'], color = color.orange, emissive=True)
moon = sphere(radius = radius['moon'],pos=center+vector(cos(theta),-sin(theta),0)*x_m, color = color.white)

earth.m=mass['earth']
sun.m=mass['sun']
moon.m=mass['moon']
 

#中心是地球與月球的質心
cen_v=vector(0,0,earth_orbit['v'])
moon.v = cen_v + vector(0, 0, -moon_orbit['v'])
earth.v  = cen_v + vector(0, 0,moon_orbit['v']*moon.m/earth.m)
nor_arr= arrow(pos=earth.pos,color=color.red,shaftwidth=radius['earth']/4)

printed=False

#motion starts
while True:
    rate(24*90)#3 month
    t_total+=dt
    #moon
    moon.a = G_force(moon.m,earth.m,moon.pos,earth.pos) / moon.m + G_force(moon.m,sun.m,moon.pos,sun.pos)/moon.m
    moon.v += moon.a * dt
    moon.pos += moon.v * dt
    
    #earth
    earth.a = G_force(earth.m,moon.m,earth.pos,moon.pos) / earth.m +G_force(earth.m,sun.m,earth.pos,sun.pos) / earth.m
    earth.v += earth.a * dt
    earth.pos += earth.v * dt
    scene.center = earth.pos
    
    #the arrow
    nor_arr.pos=earth.pos
    nor_arr.axis=norm(cross(moon.pos-earth.pos,moon.v-earth.v))*radius['earth']*4
    
    #estimate the period
    if nor_arr.axis.x<=0:
        start_new_cycle=True
    if nor_arr.axis.x>=0 and start_new_cycle==True and printed==False:
        print(2*t_total/(3600*24*365))
        start_new_cycle=False
        printed=True
        


        
    

    
