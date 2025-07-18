import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, -1, 500)
x2 = np.linspace(1, 10, 500)
a = 3
b = 2

y1 = b * np.sqrt((x**2 / a**2) - 1)
y2 = -b * np.sqrt((x**2 / a**2) - 1)

y3 = b * np.sqrt((x2**2 / a**2) - 1)
y4 = -b * np.sqrt((x2**2 / a**2) - 1)

plt.figure()
plt.plot(x, y1, 'b')
plt.plot(x, y2, 'b')
plt.plot(x2, y3, 'b')
plt.plot(x2, y4, 'b')
plt.title('Hyperbola: x²/a² - y²/b² = 1')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.show()
