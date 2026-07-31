import matplotlib.pyplot as ma
import seaborn as s
import pandas as p

df = p.read_csv("car details v4.csv")
print(df.head())

print(df.columns)

"""
Scatter Plot: A scatter plot is a graph that displays the relationship between two numerical variables using individual points, 
where each point represents one observation. It is mainly used to identify correlations, trends, and outliers in the data.

"""

da = df.loc[df["Seller Type"] == "Individual"]
den = df.loc[df["Seller Type"] == "Corporate"]
s.scatterplot(data = da , x = da["Year"], y = da["Price"], label = "Individual")
s.scatterplot(data = den , x = den["Year"], y = den["Price"], label = "Corporate")
ma.legend(loc=("upper left"))
ma.title("Individual sells vs Corporate sells Years bias")
ma.xlabel("Price")
ma.ylabel("year")
ma.show()

"""
Purpose:-
Find the relationship between two variables.
Detect patterns and trends.
Identify outliers (unusual data points).
Check whether variables are positively or negatively correlated.


"""