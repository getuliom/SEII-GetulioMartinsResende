import numpy as np
import matplotlib.pyplot as plt
from control.matlab import *

G=tf([9],[1,2,9])
print(G)

# Conversão para a representação no espaço de estados
Gss=tf2ss(G)
print(Gss)

#conversão para o tempo discreto
Ts=0.01

def rk4(tk,h,xk,uk):
    xk=xk,reshape([2,1])
    uk=uk.reshape([1,1])

    k1=Gss(tk,xk,uk)
    k2=Gss(tk + h/2.0,xk+h*k1/2.0,uk)
    k3=Gss(tk+h/2.0,xk+h*k2/2.0,uk)
    k4=Gss(tk+h,xk+h*k3,uk)

    xkp1=xk+(h/6.0)*(k1+2*k2+2*k3+k4)
    #print(xkp1.shape)

    return xkp1.reshape([2,])