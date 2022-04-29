import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import axes3d
import matplotlib.cm as cm 
import matplotlib as mpl
import numpy as np

def PS(x,y,t): 
    return np.sin(y**2 +t)+ np.cos(x**2 +t)

x=np.linspace(-np.pi, np.pi, 101)
y=np.linspace(-np.pi, np.pi, 101)
t=np.linspace(0,20,101)

X,Y= np.meshgrid(x,y)

fig=plt.figure(figsize=(12,6),dpi=100)
ax= fig.gca(projection ='3d')

def update(i):
    Z= PS(X,Y, t[i])
    ax.clear()
    ax.plot_surface(X,Y,Z, cmap= mpl.cm.viridis)
    plt.title(str(i))
    plt.xlabel('$X$', color='g')
    plt.ylabel('$X$', color='g')