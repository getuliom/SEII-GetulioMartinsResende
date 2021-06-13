import numpy as np
import matplotlib.pyplot as plt
from control.matlab import *

G=tf([9],[1,2,9])
print(G)

yout,T,xout=lsim(G)

print(yout,'\n')
print(T,'\n')
print(xout,'\n')