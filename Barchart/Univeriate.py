# Univeriate
"""
Graphs plotting based on one single veriable

"""
import matplotlib.pyplot as ma
import pandas as p

df = p.read_csv("car details v4.csv")
print(df)
data = df['Make'].unique()
print(data)

count_Make =  df["Make"].value_counts().head(10)
print(count_Make)
# Bar chart

x = count_Make.index
# taking Index from count_Make 
y = count_Make.values
# taking value from count_Make
# ma.bar(x,y)
# ma.show() 

# size manipuation
ma.figure(figsize=(12,7))
ma.bar(x,y)
ma.show() 

# rotation and change of text size
"""X_sticks"""
ma.figure(figsize=(12,7))
ma.bar(x,y)
ma.xticks(rotation = 90 , fontsize = 8  )
ma.show() 

#  Change the size and colour of the Bars
ma.figure(figsize=(12,7))
ma.bar(x,y, width=0.6, color = "red")
ma.show() 
# label & title
ma.figure(figsize=(12,7))
ma.bar(x,y)
ma.xlabel( "make" , fontsize = 8  )
ma.ylabel( "value" , fontsize = 8  )
ma.title(" The compaany who sales most", fontsize = 24)
ma.show() 
