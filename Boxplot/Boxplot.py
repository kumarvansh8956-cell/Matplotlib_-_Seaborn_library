import matplotlib.pyplot as ma
import seaborn as s
import pandas as p
 
df = p.read_csv("car details v4.csv")
print(df)

# A Box Plot is a graphical representation of the distribution of numerical data using a box and whiskers. It displays the five-number summary and helps identify outliers

dat = df["Make"].value_counts()
ma.figure(figsize=(4,7))
ma.title(" BOX plot")
s.boxplot(dat)
ma.show()
"""
Components of a Box Plot
Min ──┬─────[ Q1 | Median | Q3 ]─────┬── Max
       │                              │
   Lower Whisker                Upper Whisker

              ● = Outlier
Five-Number Summary
Minimum :- Smallest value (excluding outliers)
Q1 (First Quartile) :- 25% of data lies below it.
Median (Q2) :- Middle value (50th percentile).
Q3 (Third Quartile) :- 75% of data lies below it.
Maximum :- Largest value (excluding outliers).

"""
"""
What are Whiskers?

The whiskers are the lines extending from the box to the smallest and largest non-outlier values.

What is an Outlier?

An outlier is a value that is unusually far from the rest of the data. It is shown as a separate point (●).


"""