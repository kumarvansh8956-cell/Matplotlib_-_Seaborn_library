import matplotlib.pyplot as ma
import seaborn as s
import pandas as p

df = p.read_csv("car details v4.csv")

num_data = df.select_dtypes(include="number")
print(num_data)
s.heatmap(num_data.corr(), annot=True)
ma.show()
"""
by annot=True, now heatmap has value too

"""