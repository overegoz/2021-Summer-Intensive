import pandas as pd
from matplotlib import pyplot as plt

table = pd.read_csv('LinRegData.csv')
plt.plot(table.x_val, table.y_val, 'k.')  # k(black), .(dot)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Chart')
# plt.show()

# print(type(list(table.x_val)))
# print(list(table.x_val))

from scipy import stats, polyval
from pylab import plot, title, show, legend
import numpy as np

x, y = list(table.x_val), list(table.y_val)
slope, intercept, r_value, p_value, stderr = stats.linregress(x,y)
ry = np.polyval([slope, intercept], x)
plt.plot(x, ry, 'r-')
plt.show()

