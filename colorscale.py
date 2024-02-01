import numpy as np
import matplotlib.pyplot as plt

# Generate some example data
np.random.seed(42)
x = np.random.rand(100)
y = np.random.rand(100)
colors = np.random.rand(100)  # Example data for color scale

# Create a scatter plot with a color scale
plt.scatter(x, y, c=colors, cmap='viridis', alpha=0.7)

# Add a colorbar to show the mapping of values to colors
cbar = plt.colorbar()
cbar.set_label('Color Scale')

# Set axis labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot with Color Scale')

# Show the plot
plt.show()
