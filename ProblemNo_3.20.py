from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

theta = np.linspace(0, 2 * np.pi, 200)
x = np.sqrt(5)*np.cos(theta)
y = np.sqrt(5)*np.sin(theta)
ax.plot(x,y,np.sqrt(5/2),'g', alpha =0.6 )

len = 10
x1, x2 = np.meshgrid(np.linspace(0,5,len),np.linspace(0,5,len))
z=(x1*x2)**0.5
ax.plot_surface(x1, x2, z, color='r',alpha=0.3)

ax.plot([np.sqrt(5/2)], [np.sqrt(5/2)], [np.sqrt(5/2)], markerfacecolor='b', markeredgecolor='b', marker='o', markersize=5, alpha=0.7)

ax.set_xlabel('$X$', rotation=150)
ax.set_ylabel('$Y$')
ax.set_zlabel('$Z$', rotation=0)

ax.legend()

plt.show()
