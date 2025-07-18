import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

theta = np.linspace(0, 2 * np.pi, 100)
z = np.linspace(-5, 5, 100)
theta, z = np.meshgrid(theta, z)

a = 3
b = 1.5
x = a * np.cos(theta)
y = b * np.sin(theta)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, alpha=0.6)
ax.set_title("Jingulala Cylinder")
plt.show()
