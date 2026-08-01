import matplotlib.pyplot as ma
import seaborn as s
import pandas as p

df = p.read_csv("car details v4.csv")
# Heatmap: A visualization that represents data values using colors.
# It is commonly used to display correlations, patterns, and trends,
# where darker or warmer colors indicate higher values and lighter
# or cooler colors indicate lower values.

num_data = df.select_dtypes(include="number")
print(num_data)
s.heatmap(num_data.corr())
# or s.heatmap(num_data.corr(), annot= False)
# annot = False (default)

ma.show()

"""
Use a heatmap when you want to:

✅ Find correlations between numerical features.
✅ Identify patterns in a matrix or pivot table.
✅ Spot high and low values instantly using colors.
✅ Detect multicollinearity before building ML models.

"""