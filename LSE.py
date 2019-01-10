import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from sklearn import datasets, linear_model
from numpy.polynomial.polynomial import polyfit

a = pd.read_csv("./set-a/132539.txt")

HR = np.array(a[a.Parameter == 'HR'].Value)
RR = np.array(a[a.Parameter == 'RespRate'].Value)

# taking care of missing data
for x in range(37,42):
 HR = np.append(HR,HR.mean())

# For Plot
x = HR
y = RR

# Plot outputs
plt.scatter(x,y, color='blue')
plt.title('SCATTER PLOT')
plt.xlabel('HR')
plt.ylabel('RESP RATE')
plt.xticks(())
plt.yticks(())
plt.show()

# Fit with polyfit
b, m = polyfit(x, y, 1)

plt.figure(figsize=(6,4))
plt.plot(x, y, '.')
plt.plot(x, b + m * x, color='yellow')
plt.title('LSE FIT')
plt.xlabel(r'$HR$')
plt.ylabel(r'$RespRate$')
plt.show()
