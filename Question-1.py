import numpy as np
import matplotlib.pyplot as plt

# Ellipse equation: x^2/5 + y^2/16 = 1
a2 = 5   # Denominator of x^2
b2 = 16  # Denominator of y^2

a = np.sqrt(a2)  # Semi-minor axis (along x-axis)
b = np.sqrt(b2)  # Semi-major axis (along y-axis)

# Distance from center to each focus
c = np.sqrt(b**2 - a**2)

# Center and foci of the ellipse
center = (0, 0)
foci = [(0, -c), (0, c)]  # Along y-axis

# Print results
print(f"Center of the ellipse: {center}")
print(f"Semi-major axis (b): {b}")
print(f"Semi-minor axis (a): {a}")
print(f"Foci: {foci}")

# Generate ellipse points
theta = np.linspace(0, 2 * np.pi, 1000)
x = a * np.cos(theta)
y = b * np.sin(theta)

# Plotting
plt.figure(figsize=(6, 6))
plt.plot(x, y, label='Ellipse')
plt.scatter(*center, color='red', label='Center')
plt.scatter([f[0] for f in foci], [f[1] for f in foci], color='blue', label='Foci')

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Ellipse: x²/5 + y²/16 = 1')
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
import numpy as np
import matplotlib.pyplot as plt

# Ellipse equation: x^2/5 + y^2/16 = 1
a2 = 5   # Denominator of x^2
b2 = 16  # Denominator of y^2

a = np.sqrt(a2)  # Semi-minor axis (along x-axis)
b = np.sqrt(b2)  # Semi-major axis (along y-axis)

# Distance from center to each focus
c = np.sqrt(b**2 - a**2)

# Center and foci of the ellipse
center = (0, 0)
foci = [(0, -c), (0, c)]  # Along y-axis

# Print results
print(f"Center of the ellipse: {center}")
print(f"Semi-major axis (b): {b}")
print(f"Semi-minor axis (a): {a}")
print(f"Foci: {foci}")

# Generate ellipse points
theta = np.linspace(0, 2 * np.pi, 1000)
x = a * np.cos(theta)
y = b * np.sin(theta)

# Plotting
plt.figure(figsize=(6, 6))
plt.plot(x, y, label='Ellipse')
plt.scatter(*center, color='red', label='Center')
plt.scatter([f[0] for f in foci], [f[1] for f in foci], color='blue', label='Foci')

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Ellipse: x²/5 + y²/16 = 1')
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
