import matplotlib.pyplot as ma
import seaborn as s
import pandas as p
 
df = p.read_csv("car details v4.csv")
print(df)

dat = df["Make"].value_counts()
ma.figure(figsize=(4,7))
ma.title(" BOX plot")
ma.boxplot(dat)
ma.show()
