import numpy as np
import matplotlib.pyplot as plt

# Define the function r = 20 * (tan(17t) + cot(17t))
def r_function(t):
    return 20 * (np.tan(17 * t) + 1 / np.tan(17 * t))

# Generate values for t
t_values = np.linspace(0, 2 * np.pi, 1000)

# Compute r values
r_values = r_function(t_values)

# Create the polar plot
plt.figure(figsize=(8, 8))
ax = plt.subplot(111, projection='polar')

# Plot the function
ax.plot(t_values, r_values, label=r'$r = 20(\tan(17t) + \cot(17t))$')

# Add a legend
ax.legend(loc='upper right')

# Add a title
ax.set_title('Polar Plot of $r = 20(\tan(17t) + \cot(17t))$')

# Display the plot
plt.show()
