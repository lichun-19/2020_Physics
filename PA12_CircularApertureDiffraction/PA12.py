from vpython import *
from numpy import *
N = 100
R, lamda = 1.0, 500E-9
d = 100E-6
dx, dy = d/N, d/N
k=2*pi/lamda

scene1 = canvas(align = 'left', height=600, width=600, center = vector(N*dx/2, N*dy/2, 0))
scene2 = canvas(align = 'right', x=600, height=600, width=600, center = vector(N*dx/2, N*dy/2, 0))
scene1.lights, scene2.lights = [], []
scene1.ambient, scene2.ambient = color.gray(0.99), color.gray(0.99)

side = linspace(-0.01*pi, 0.01*pi, N)
x,y = meshgrid(side,side)

# change this to calculate the electric field of diffraction of the aperture
A=zeros((N,N))
for i in range(N):
        for j in range(N):
                if ((i-N/2)**2+(j-N/2)**2)<= (N/2)**2:
                        A+=(cos(k/R*x*dx*(i-N/2)+k/R*y*dy*(j-N/2)))/R

E_field = A

Inte = abs(E_field) ** 2

maxI = amax(Inte)
for i in range(N):
        for j in range(N):
                box(canvas = scene1, pos=vector(i*dx, j*dy, 0), length = dx, height= dy, width = dx,
                        color=vector(Inte[i,j]/maxI,Inte[i,j]/maxI,Inte[i,j]/maxI))


p_min=0
for i in range (int(N/2)):
        if Inte[int(N/2),int(N/2)+i]<=Inte[int(N/2),int(N/2)+p_min]:
                p_min=i
        else:
                break
r_dark=(p_min)*2*pi/N*0.01


Inte = abs(E_field)
maxI = amax(Inte)

for i in range(N):
        for j in range(N):
                box(canvas = scene2, pos=vector(i*dx, j*dy, 0), length = dx, height= dy, width = dx,
                        color=vector(Inte[i,j]/maxI,Inte[i,j]/maxI,Inte[i,j]/maxI))


#find and print the radius of the first dark ring and check whether the Rayleigh criterion is satisfied.
print ("radius of the first dark ring=",r_dark )
print("experimental theta",arctan(r_dark/R))
print("theoretical theta (1.22*lamda/d)=",1.22*lamda/d)
