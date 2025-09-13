import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


data = np.random.rand(10,10)

sns.heatmap(data)
plt.title("Heatmap Example")

#theta = np.linspace(0, 2*np.pi, 100)
#r = np.sin(6*theta)

#plt.polar(theta, r)
#plt.title("Polar plot")

plt.show()