import numpy as np
import matplotlib.pyplot as plt

r = 5  # radius
theta = np.linspace(0, 2 * np.pi, 1000)
x = r * np.cos(theta)
y = r * np.sin(theta)

plt.figure()
plt.plot(x, y)
plt.gca().set_aspect('equal', adjustable='box')
plt.title('Circle: x² + y² = r²')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
