### 01 Visualizing data with python

# lots of tools but matplotlib a clear winner in popularity

### 02 Matplotlib pattern

# import needed package
import matplotlib.pyplot as plt

# Initialize the chart with subplots
fig, ax = plt.subplots()
# fill the axes
ax.plot([1,2,3,4,5], [2,3,1,4,5])
# show the plot
plt.show()


# scatter example
fig, ax = plt.subplots()
ax.scatter([1,2,3,4,5], [2,3,1,4,5])
plt.show()

### 03 Pyplot VS axes

# pyplot interface
import matplotlib.pyplot as plt

plt.plot([1,2,3,4,5], [2,3,1,4,5])
plt.show()

# Axes interface is the way to go

### 04 What on earth are Figure, Axes, and Subplot?!

# Axes
# The Axes is where the actual data visualization happens—it contains the plot elements such as lines, bars, scatter points, and more.

# Figure
# A Figure is the top-level container for everything in a Matplotlib chart. Think of it as the canvas where all elements are drawn, including one or more Axes.
# One figure can have several axes

# Adding text
# It requires at least three arguments: x: the position on the x-axis, y: the position on the y-axis, s: the text content
# ax.text(x, y, s): adds text to the Axes
# fig.text(x, y, s): adds text to the Figure

# Axes and Figure: Different Coordinate Systems 
# Axes use the same coordinate system as the data (i.e., data coordinates).
# Figure coordinates range from 0 to 1 on both the x and y axes.

# Conclusion
# Every Matplotlib visualization is a Figure with one or more Axes.
# A Figure is the overall container for all elements, including Axes and other graph components. Its coordinates range from 0 to 1 on both x and y axes.
# An Axes is a container for displaying a single chart (line chart, bar plot, etc.), with coordinates in the same scale as the data.
# When a Figure has a single Axes (as in every chart we've made so far), the center of the Axes and the Figure align.

### 05 Build (almost) any chart type

# Matplotlib methods

# Plotting
# fundamental functions for creating chart types, like hist() for histograms, scatter() for scatterplots,bxp() for boxplots, and more.

# Text and Annotations
# Annotation is critical in data visualization, and we'll spend a lot of time adding text (e.g., ax.text), arrows, lines, and other shapes to enhance the insights a graph provides.

# Axis limits, direction and scale
# These functions not only manage the x and y axis limits but also allow us to change the scale to logarithmic, quasi-logarithmic, logit, and more.