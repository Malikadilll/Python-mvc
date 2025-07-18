import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 400)
y = x**2 / 4  # y² = 4ax form (standard parabola)

plt.figure()
plt.plot(x, y)
plt.title('Parabola: y = x² / 4')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.show()
