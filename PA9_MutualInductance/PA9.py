from vpython import*
import numpy as np


R1=0.12 #standard unit
R2=0.06
h=0.1
u0=pi*4E-7
I=1
N=1
n=1000
m=1000
d_theta=2*pi/n
theta=np.array([d_theta*i for i in range(n)])

def BS_Law(i,ds,r):
        #i=current ; ds=line segment vector ; dr=distance vector
        dB=u0*i*cross(ds,r.norm())/(4*pi*r.mag**2)
        return dB

#Mag Field at point P
def Mag_Field(p_pos,ds_pos,ds_vec,I):
        B_of_P=vec(0,0,0)
        for i in range(n):
                B_of_P+=BS_Law(I,ds_vec[i],ds_pos[i]-p_pos)
        return B_of_P

#sum the Mag Field of points
def total_M(ring_E_radius,ring_E_hight,ring_radius,ring_height):
        ds_mag=2*pi*ring_E_radius/n
        ds_vec=[vec(-ds_mag*sin(theta[i]),ds_mag*cos(theta[i]),0) for i in range(n)]
        ds_pos=[vec(ring_E_radius*cos(theta[i]),ring_E_radius*sin(theta[i]),ring_E_hight) for i in range(n)]

        total_flux=0
        for j in range(m):
                p_pos=vec(ring_radius*(j+0.5)/m,0,ring_height)
                d_area_vec=pi*vec(0,0,(ring_radius*(j+1)/m)**2-(ring_radius*(j)/m)**2)
                total_flux+=dot(Mag_Field(p_pos,ds_pos,ds_vec,I),d_area_vec)
        return total_flux

M1=total_M(R1,0,R2,h)*N/I
M2=total_M(R2,h,R1,0)*N/I

print("magnetic flux in small loop=",M1,"magnetic flux in large loop=",M2)




