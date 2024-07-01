import matplotlib.pyplot as plt
import numpy as np

# Generate sample data
x = np.linspace(0, 10, 100)
num_lines = 30
y_offsets = np.linspace(0, 10, num_lines)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Define colors
colors = plt.cm.viridis(np.linspace(0, 1, num_lines))

# Plot multiple lines
for i, offset in enumerate(y_offsets):
    y = np.sin(x) + offset  # Example data, you can customize this
    ax.plot(x, y, color=colors[i], alpha=0.7)

# Add grid
ax.grid(False)

# Remove axis
ax.axis('off')

# Set background color
fig.patch.set_facecolor('white')

# Save the plot as an image
plt.savefig("layered_lines.png", bbox_inches='tight', pad_inches=0.1, dpi=300)

# Show the plot
plt.show()
