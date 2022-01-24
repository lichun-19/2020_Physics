from vpython import *

#constants
R = 4.0
thickness = 0.3
g1center = vec(-R + thickness/2, 0, 0) #right-plane
g2center = vec(R - thickness/2, 0, 0) #left-plane
nair = 1
nglass = 1.5

#beckground setting
scene = canvas(background=vec(0.8, 0.8, 0.8), width=1200, height=300, center = vec(3,0,10), fov = 0.004)
lens_surface1 = shapes.arc(radius=0.15, angle1=0, angle2=pi)
circle1 = paths.arc(pos=vec(0, 0, 0), radius=0.0000001, angle2=2*pi, up = vec(1,0,0))
lens_surface2 = shapes.arc(radius=0.15, angle1=-pi, angle2=0)
circle2 = paths.arc(pos=vec(0, 0, 0), radius=0.0000001, angle2=2*pi, up = vec(1,0,0))
extrusion(path=circle1, shape=lens_surface1, color=color.yellow, opacity = 0.5)
extrusion(path=circle2, shape=lens_surface2, color=color.yellow, opacity = 0.5)
curve(pos=[vec(-7,0,0),vec(13,0,0)], color=color.red, radius = 0.02)

#objet & image
arrow(pos=vec(-6,0,0), axis=vec(0,0.5,0), shaftwidth=0.1)
arrow(pos=vec(12, 0, 0), axis=vec(0, -1, 0), shaftwidth = 0.1)


def refraction_vector(n_origin, n_prime, v_in, normal_v):
        theta_i=acos(dot(v_in,normal_v))  #magnitude=1
        theta_r=asin(n_origin/n_prime*sin(theta_i))
        if(cross(v_in,normal_v).z>=0):
                v_out=rotate(normal_v,angle=-theta_r ,axis=vec(0,0,1))
        else:
                v_out=rotate(normal_v,angle=theta_r ,axis=vec(0,0,1))
        
        return v_out



for angle in range(-7, 2):
        state=0
        ray = sphere (pos=vec(-6, 0.5, 0), color = color.blue, radius = 0.01, make_trail=True) 
        ray.v = vector (cos(angle/40.0), sin(angle/40.0), 0) #on xy plane
        dt = 0.002

        while True:
                rate(1000)
                ray.pos = ray.pos + ray.v*dt

                if ((ray.pos-g2center).mag<=R and state==0):#left-plane
                        state=1
                        ray.v=refraction_vector(nair, nglass, ray.v, norm(g2center-ray.pos))
                        
                if ((ray.pos-g1center).mag>=R and state==1):#right-plane
                        state=2
                        ray.v=refraction_vector(nglass, nair, ray.v, norm(ray.pos-g1center))
                
                
                # your code here
                if ray.pos.x >= 12:
                        print(ray.pos.y)
                        break
          
