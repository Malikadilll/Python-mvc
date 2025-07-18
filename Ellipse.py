import numpy as np
import matplotlib.pyplot as plt

a = 5  # semi-major
b = 3  # semi-minor
theta = np.linspace(0, 2 * np.pi, 1000)
x = a * np.cos(theta)
y = b * np.sin(theta)

plt.figure()
plt.plot(x, y)
plt.gca().set_aspect('equal', adjustable='box')
plt.title('Ellipse: x²/a² + y²/b² = 1')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
