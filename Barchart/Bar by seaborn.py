import seaborn as s
import pandas as p
import matplotlib.pyplot as m


"""
# ======================= Seaborn Notes =======================

# 1. countplot()
# -> Use when you want Seaborn to count the categories automatically.
# -> Just provide the column name and the DataFrame.
#
# Example:
# sns.countplot(x="Make", data=df)

# 2. barplot()
# -> Use when you have already calculated the values
#    (using value_counts(), groupby(), mean(), etc.).
#
# Example:
# counts = df["Make"].value_counts()
# sns.barplot(x=counts.index, y=counts.values)

# 3. Top N categories
# -> First get the top categories, then pass them to 'order'.
#
# top5 = df["Make"].value_counts().head().index
# sns.countplot(x="Make", data=df, order=top5)

# Easy Rule:
# countplot() -> Seaborn counts for you.
# barplot()   -> You provide the calculated values.



"""


# this is seaborn graph ploting

df = p.read_csv("car details v4.csv")

s.countplot(x="Make", data = df , color = "green")
m.show()

#  for only top five or any specific position

top5 =  df["Make"].value_counts().head().index
s.countplot(
  x="Make",
  data = df,
  order= top5,
  color= "black"
)
m.show()