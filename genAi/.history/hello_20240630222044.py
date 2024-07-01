import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a new figure
fig, ax = plt.subplots(figsize=(8, 10))

# Set the aspect of the plot to be equal
ax.set_aspect('equal')

# Function to draw an abstract apple shape
def draw_apple(x, y, color, fill_color=None):
 apple_shape = patches.PathPatch(
patches.Path(
[(x, y), (x + 0.1, y + 0.2), (x + 0.3, y + 0.1), (x + 0.2, y - 0.2),
(x - 0.1, y - 0.3), (x - 0.3, y - 0.1), (x - 0.2, y + 0.1)],
[patches.Path.MOVETO, patches.Path.LINETO, patches.Path.LINETO, patches.Path.LINETO,
patches.Path.LINETO, patches.Path.LINETO, patches.Path.CLOSEPOLY]
),
edgecolor=color,
facecolor=fill_color if fill_color else 'none',
lw=2
)
ax.add_patch(apple_shape)

# Function to draw a small colored dot inside the apple
def draw_dot(x, y, color):
 dot = patches.Circle((x, y), 0.05, color=color)
ax.add_patch(dot)

# Drawing the apples with dots
positions = [
(0.2, 0.8, 'blue'),
(0.8, 0.8, None),
(1.4, 0.8, None),
(0.2, 0.6, 'orange'),
(0.8, 0.6, 'red'),
(1.4, 0.6, 'green'),
(0.2, 0.4, 'blue'),
(0.8, 0.4, None),
(1.4, 0.4, 'pink'),
(0.2, 0.2, None),
(0.8, 0.2, None),
(1.4, 0.2, None),
]

# Draw each apple with its dot
for pos in positions:
  draw_apple(pos[0], pos[1], 'purple')
if pos[2]:
  draw_dot(pos[0], pos[1], pos[2])

# Draw the circles around specific apples
circle1 = patches.Circle((0.2, 0.8), 0.4, edgecolor='green', facecolor='none', lw=2)
circle2 = patches.Circle((0.2, 0.8), 0.5, edgecolor='red', facecolor='none', lw=2)
ax.add_patch(circle1)
ax.add_patch(circle2)

circle3 = patches.Circle((0.2, 0.4), 0.4, edgecolor='red', facecolor='none', lw=2)
ax.add_patch(circle3)

# Hide the axes
ax.axis('off')

# Display the plot
plt.show()