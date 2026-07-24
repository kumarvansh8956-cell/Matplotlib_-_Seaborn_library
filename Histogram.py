# Histogram
"""
A histogram is a graph that groups numerical data into intervals (bins) and shows how many values fall into each interval
"""
# It helps answer questions like:
"""

 Where are most values concentrated?
 Is the data spread out or clustered?
 Is the distribution symmetric or skewed?
 Are there any unusual values (possible outliers)?

"""
import matplotlib.pyplot as ma
import pandas as p

df = p.read_csv("car details v4.csv")
print(df.T.head(10))

data = df.groupby("Year")["Make"].count()                    
print(data)


# histogram
ma.hist(data, bins = 10)

ma.show()

"""
A histogram tells how many observations (such as years, students, employees, etc.) fall into each range (bin).

"""
#  length of bins :
#   number_of_bins + 1
#     10 + 1 = 11