from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
# Leyenda de inicialización
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#Establecer el valor de X, Y

r = [2,2]
p = np.linspace(0, 2*np.pi, 64)
R, P = np.meshgrid(r, p)
X, Y = R * np.cos(P), R * np.sin(P)
r1=[1,0]
#Establecer el alcance de Z
ax.set_zlim(0, 10)
try:
    while True:
        #Borrar imagen original
        plt.cla()
        p1 = np.random.randint(10, size=64)
        R1, P1 = np.meshgrid(r1, p1)
        # Establecer valor Z
        Z = R1*P1
        #Dibujar imagen 3D
        ax.plot_surface(X, Y, Z, cmap=plt.cm.plasma)
        # Actualice continuamente la imagen haciendo una pausa y borrándola para formar una imagen en movimiento
        plt.pause(0.5)
except:
    pass