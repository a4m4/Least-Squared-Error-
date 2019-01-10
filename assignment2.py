import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from numpy.polynomial.polynomial import polyfit

a = pd.read_csv("./set-a/132539.txt")

HR = np.array(a[a.Parameter == 'HR'].Value)
RR = np.array(a[a.Parameter == 'RespRate'].Value)

