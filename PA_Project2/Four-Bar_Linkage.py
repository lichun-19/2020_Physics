from vpython import *

canvas(width = 1200, height = 800, center = vector(0, 0, 0), background = color.white)
k=1
r1 = 2.8*k
r2 = 1.3*k
r3 = 3*k
r4 = 3*k
n = 3 # round/min

# initial condition 
dt = 0.005
omega = n / 60 * 360 * pi / 180
find_theta_prime=0
d_theta=-pi/1000

def find_deadpoint(L1, L2):
     theta = acos((L1**2 + r4**2 - L2**2)/(2*L1*r4))*L1/abs(L1)
     return theta

def get_p_3(p2, p4):
        temp_point = vector (p4.pos+vector(r3,0,0))
        global find_theta_prime
        global d_theta
        find_theta=find_theta_prime
        #KEY: Find the nearest
        for i in range(2000) :
                temp_point = p4.pos+vector(r3*cos(find_theta),r3*sin(find_theta),0)
                if find_theta_prime==0 and sin(find_theta)<0 and alpha_1!=0:
                        find_theta+=d_theta
                elif abs(mag(temp_point-p2.pos)-r2)<=0.01:
                        find_theta_prime=find_theta
                        break
                else:
                        find_theta+=d_theta

        return temp_point

#deadpoints
try:
     alpha_1 = find_deadpoint(r1-r2, r3)
except ValueError:
     alpha_1 = 0
     
try:
     alpha_2 = find_deadpoint(r1+r2, r3)
except ValueError:
     alpha_2 = 0
     
try:
     betta_1 = find_deadpoint(r1, r2+r3)
except ValueError:
     betta_1 = 0
     
try:
     betta_2 = find_deadpoint(r1, r3-r2)
except ValueError:
     betta_2 = 0

p1 = sphere(pos = vector(r1 * cos(alpha_1), r1 * sin(alpha_1), 0), radius = 0.06, color = color.yellow)#fixed
p2 = sphere(pos = vector(r1 * cos(alpha_2), r1 * sin(alpha_2), 0), radius = 0.06, color = color.yellow)
p3 = sphere(pos = vector(r1 * cos(betta_1), r1 * sin(betta_1), 0), radius = 0.06, color = color.blue)#fixed
p4 = sphere(pos = vector(r1 * cos(betta_2), r1 * sin(betta_2), 0), radius = 0.06, color = color.blue)
print(alpha_1, alpha_2,betta_1, betta_2)

# initial shape
theta0 = betta_1
point1 = sphere(pos = vector(0, 0, 0), radius = 0.06, color = color.red)#fixed
point2 = sphere(pos = vector(r1 * cos(theta0), r1 * sin(theta0), 0), radius = 0.06, color = color.red)
point4 = sphere(pos = vector(r4, 0, 0), radius = 0.06, color = color.red)#fixed
point3 = sphere(pos = get_p_3(point2,point4), radius = 0.06, color = color.green, make_trail=True)
point5 = sphere(pos = get_p_3(point2,point4), radius = 0.1, color = color.red)

trail = ring(pos = vector(0, 0, 0), axis = vector(0, 0, 1), radius = r1, thickness = 0.01, color = color.blue)
trail = ring(pos = point4.pos, axis = vector(0, 0, 1), radius = r3, thickness = 0.01, color = color.blue)
x_axis = arrow(pos=vector(-2, 0, 0), axis=vector(6, 0, 0), shaftwidth=0.02, color = color.black)
y_axis = arrow(pos=vector(0, -2, 0), axis=vector(0, 4, 0), shaftwidth=0.02, color = color.black)
rod1 = cylinder(pos = point1.pos, axis = vector(point2.pos-point1.pos), radius = 0.02, color = color.blue)
rod2 = cylinder(pos = point2.pos, axis = -vector(point2.pos-point3.pos), radius = 0.02, color = color.blue)
rod3 = cylinder(pos = point3.pos, axis = -vector(point3.pos-point4.pos), radius = 0.02, color = color.blue)
rod4 = cylinder(pos = point4.pos, axis = -vector(point4.pos-point1.pos), radius = 0.02, color = color.blue)

theta = theta0
flag = 1
for i in range(10000):
	rate(400)
	theta += omega * dt
	if (alpha_1==0 and betta_1==0):
		d_theta=pi/1000 
	if (alpha_1!=0 and betta_1==0):
		if sin(theta) > sin(alpha_2) and flag==1:
			d_theta = -d_theta
			flag = 2
		if sin(theta) < sin(alpha_1) and flag==2:
			d_theta = -d_theta
			flag = 1
        
	if (alpha_1!=0 and betta_1!=0):
		if theta > betta_1 and flag==1:
			omega = -omega
			theta += 2*omega*dt
			flag = 2
		if theta < alpha_2 and flag==2:
			d_theta = -d_theta
			flag = 3
		if theta < betta_2 and flag==3:
			omega = -omega
			theta += 2*omega*dt
			flag = 4
		if theta > alpha_1 and flag==4:
			d_theta = -d_theta
			flag = 1
	
	'''
	if theta <= max(alpha_1, alpha_2) and min(alpha_1, alpha_2):
		if flag_betta==True:
			flag_alpha = True
		
	if (theta > alpha_1 or theta < alpha_2) and flag_alpha and flag_betta:
		d_theta = -d_theta
		flag_alpha = False
		flag_betta = False
                
	if theta > betta_1 or theta < betta_2:
		omega = -omega
		theta += 2*omega*dt
		flag_betta = True
	'''
	point2.pos = vector(r1 * cos(theta), r1 * sin(theta), 0)
	point3.pos = get_p_3(point2,point4)
	rod1.axis = vector(point2.pos-point1.pos)
	rod2.pos = point2.pos
	rod2.axis = -vector(point2.pos-point3.pos)
	rod3.pos = point3.pos
	rod3.axis = -vector(point3.pos-point4.pos)

