import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(-2, 2, 100)
u, v = np.meshgrid(u, v)

a = 1
b = 1
c = 1
x = a * np.cosh(v) * np.cos(u)
y = b * np.cosh(v) * np.sin(u)
z = c * np.sinh(v)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='coolwarm', alpha=0.7)
ax.set_title("Hyperboloid of One Sheet")
plt.show()
