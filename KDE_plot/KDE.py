import matplotlib.pyplot as ma
import seaborn as s
import pandas as p

df = p.read_csv("car details v4.csv")
print(df.T.head(10))

data = df.groupby("Year")["Make"].count()

"""
A KDE (Kernel Density Estimation) Plot is a statistical graph that estimates and displays the probability density of continuous data as a smooth curve.

"""

s.kdeplot(data)
ma.show()

"""
| Histogram                      | KDE Plot                                      |
| ------------------------------ | --------------------------------------------- |
| Uses bars                      | Uses a smooth curve                           |
| Shows frequency of data        | Shows probability density                     |
| Uses bins                      | Does not use bins                             |
| Good for counting observations | Good for visualizing the overall distribution |




"""
# skewness

"""
1. Symmetrical (Zero Skewness)
   * Left and right sides are equal.
   * Mean ≈ Median ≈ Mode.
   * Bell-shaped curve.
        /\
      /    \
_____/      \_____
2. Positive Skewness (Right-Skewed)
     * The tail extends to the right.
     * Most values are on the left.
     * A few large values pull the distribution to the right.
      /\
    /   \______
___/           \____

Relationship:

Mean > Median > Mode

Example:

Income of people (a few very high incomes).
3. Negative Skewness (Left-Skewed)
   * The tail extends to the left.
   * Most values are on the right.
   * A few small values pull the distribution to the left.
        /\
   ____/   \
__/         \____

Relationship:

Mean < Median < Mode

Example:

Easy exam marks (most students score high).


"""