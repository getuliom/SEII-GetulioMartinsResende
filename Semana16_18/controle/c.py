import numpy as np
import matplotlib.pyplot as plt
from control.matlab import *

G=tf([9],[1,2,9])
print(G)

# Conversão para a representação no espaço de estados
Gss=tf2ss(G)
print(Gss)

rlist,klist=rlocus(G)

#conversão para o tempo discreto

Ts=0.01
Gd=c2d(G,Ts,method='tustin')

#PID

Kp=150
Ki=30
Kd=20

P=tf([Kp],[1],Ts)
I=(Ki*Ts/2)*tf([1,1],[1,-1],Ts)
D=(2*Kd/Ts)*tf([1,-1],[1,1],Ts)

print('--> P\n',P,'\n-->I\n',I,'\n-->D\n',D)

Cz=P+I+D

print('\n-->PID\n',Cz)

T=feedback(Cz*Gd)
yout,tout=step(T)
plt.plot(tout,yout)
