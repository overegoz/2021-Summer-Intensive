import pandas as pd
from matplotlib import pyplot as plt

table = pd.read_csv('data-label.csv')
plt.plot(table.wavelength, table.value)
plt.xlabel('wavelength')
plt.ylabel('value')
plt.title('Measurement')
plt.show()

