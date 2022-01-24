from vpython import*

#constants 
Fd=120 #Hz
omega=Fd*2*pi
T=1/Fd

R=30
L=0.2
C=20E-6

Zr=complex(R,0)
ZL=complex(0,omega*L)
Zc=complex(0,-1/(omega*C))
Ztotal=Zr+ZL+Zc

#variables
v_source=0
i_current=0
E_in=0
Q=0
t=0
dt = 1.0/(Fd * 5000) # 5000 simulation points per cycle

#theoretical 
i_theo=(36/Ztotal)
i_max_theo=abs(i_theo)
phi_theo=(atan(i_theo.imag/i_theo.real))*180/pi


#background setting
scene1 = graph(align = 'left', xtitle='T', ytitle='i (A) blue, v (100V) red,', background=vector(0.2, 0.6, 0.2))
scene2 = graph(align = 'left', xtitle='T', ytitle='Energy (J)', background=vector(0.2, 0.6, 0.2))
i_t = gcurve(color=color.blue, graph = scene1)
v_t = gcurve(color=color.red, graph = scene1)
E_t = gcurve(color=color.red, graph = scene2)


t_decay=0
E_at_12T=0
check=False
i_max,v_max=0,0
i_max_t,v_max_t=0,0

#start
while(t<=20*T):
        rate(5000)
        
        t+=dt
        if(t<=12*T):
                v_source=36*complex(sin(omega*t),cos(omega*t))
        else:
                v_source=complex(0,0)
        
        Vr=i_current*Zr
        Vc=Q/C
        VL=v_source-Vr-Vc
        
        i_current+=VL*dt/L
        Q+=i_current*dt
        E_in=C*(Vc.real)**2/2+L*i_current.real**2/2

        #plot
        i_t.plot(pos=(t/T,i_current.real))
        v_t.plot(pos=(t/T,v_source.real/100))
        E_t.plot(pos=(t/T,E_in))

        #find Amplitude of Current and Phase Constant
        if(8*T<t<=9*T):
                if(i_current.real>i_max):
                        i_max=i_current.real
                        i_max_t=t
                if(v_source.real>v_max):
                        v_max=v_source.real
                        v_max_t=t
                phi=(v_max_t-i_max_t)*360/T

        #find Decay Time
        if(t>=12*T and (t-12*T)<=dt):
                E_at_12T=E_in
        if(E_in<=0.1*E_at_12T and t>12*T and check==False):
                t_decay=t-12*T
                check=True


print("Amplitude of Current(theoretical)=",i_max_theo)
print("Amplitude of Current=",i_max)
print("Phase Constant(theoretical)=",phi_theo)
print("Phase Constant=",phi)
print("Decay Time=",t_decay)


