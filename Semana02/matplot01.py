import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd

x=[0,1,2,3,4]
y=[0,2,4,6,8]

# Resize your Graph (dpi specifies pixels per inch. When saving probably should use 300 if possible)
plt.figure(figsize=(5,3),dpi=300)

# Line 1

#keyword argument notation
#plt.plot(x,y,label='2x',color='red',linewidth=2,marker='.',linestyle='--',markersize=10,markeredgecolor='blue')

# Shorthand notation
#fmt='[color][marker][line]'
plt.plot(x,y,'b*--',label='2x')

## Line 2

# select inteval we want to plot points at
x2=np.arange(0,4.5,0.5)

# Plot part of the graph as line
plt.plot(x2[:5],x2[:5]**2,'r',label='x²')

# Plot part of the graph as a dot
plt.plot(x2[4:],x2[4:]**2,'r--')

# Add a title (specify font parameters with fontdict)
plt.title('Our first Graph!',fontdict={'fontname':'Comic Sans MS','fontsize':20})

# X and Y labels
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# X and Y axis Tickmarks (scale of your graph)
plt.xticks([0,1,2,3])
#plt.yticks([0,2,4,6,8,10])

# Add a legend
plt.legend()

# Save figure (dpi 300 is good when saving so graph has high resolution)
plt.savefig('mygraph.png',dpi=300)

# Show plot
plt.show()