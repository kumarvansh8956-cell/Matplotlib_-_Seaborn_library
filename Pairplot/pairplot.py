# Pairplot: A Seaborn plot that displays pairwise relationships between
# numerical features in a dataset. It shows scatter plots for each pair
# of variables and histograms (or KDE plots) on the diagonal, helping
# identify patterns, correlations, distributions, and outliers.

import matplotlib.pyplot as ma
import seaborn as s
import pandas as p

df = p.read_csv("car details v4.csv")

num_data = df.select_dtypes(include="number")
print(num_data)
s.pairplot(num_data.corr())
ma.show()