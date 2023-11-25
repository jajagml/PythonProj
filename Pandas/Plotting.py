import pandas as pd
import matplotlib.pyplot as plt

# Plot - part of pandas responsible in creating diagram
# using Pyplot (submodule of Matplotlib library) to visualize the diagram on the screen

myVar = pd.read_csv('Pandas\\data3.csv')
# myVar.plot()
# plt.show()

# Scatter Plot
# myVar.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
# plt.show()

# Histogram plot
myVar['Duration'].plot(kind = 'hist')
plt.show()