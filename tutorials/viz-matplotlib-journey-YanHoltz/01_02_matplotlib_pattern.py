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