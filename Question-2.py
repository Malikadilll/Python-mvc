import numpy as np
import matplotlib.pyplot as plt

# Ellipse equation: x^2/25 + y^2/4 = 1
a = 5  # Semi-major axis (x-direction)
b = 2  # Semi-minor axis (y-direction)

# Focal distance
c = np.sqrt(a**2 - b**2)

# Center and foci
center = (0, 0)
foci = [(c, 0), (-c, 0)]  # Along x-axis

# Print details
print(f"Center: {center}")
print(f"Semi-major axis (a): {a}")
print(f"Semi-minor axis (b): {b}")
print(f"Foci: {foci[0]}, {foci[1]}")

# Generate points for the ellipse
theta = np.linspace(0, 2 * np.pi, 1000)
x = a * np.cos(theta)
y = b * np.sin(theta)

# Plotting
plt.figure(figsize=(6, 6))
plt.plot(x, y, label="Ellipse", color="blue")
plt.scatter(*center, color='red', label="Center")
plt.scatter([f[0] for f in foci], [f[1] for f in foci], color='green', label="Foci")

plt.xlim(-6, 6)
plt.ylim(-3, 3)
plt.gca().set_aspect('equal', adjustable='box')
plt.title("Ellipse: x²/25 + y²/4 = 1")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()
