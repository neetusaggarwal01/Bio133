# Let's make a standard curve plotting with matplotlib
import matplotlib.pyplot as plt

x = [3.5710, 2.3470, 1.7710, 1.4875, 1.2930,
     1.1645, 1.1125, 1.0855]  # x axis values
# corresponding y axis values
y = [1000, 500, 250, 125, 62.5, 31.25, 15.625, 0]

plt.plot(x, y)  # plotting the points in line format

plt.xlabel('Absorbance')  # naming the x axis

plt.ylabel('Protein Concentration')  # naming the y axis

# give a title to your graph (note: it automatically puts the title on top)
plt.title('BSA Standard Curve')

plt.show()  # function to show the plot
