import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd

x=[0,1,2,3,4]
y=[0,2,4,6,8]
#plt.plot(x,y,label='2x',color='red',linewidth=2,marker='.',linestyle='--',markersize=10,markeredgecolor='blue')
# Use shorthand notation
#fmt='[color][marker][line]'
plt.plot(x,y,'b*--',label='2x')

plt.title('Our first Graph!',fontdict={'fontname':'Comic Sans MS','fontsize':20})
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.xticks([0,1,2,3])
plt.yticks([0,2,4,6,8,10])

plt.legend()

plt.show()