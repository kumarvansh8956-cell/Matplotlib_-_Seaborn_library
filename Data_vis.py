import matplotlib.pyplot as m
import seaborn as s

x = [1,2,3,4,4,5]
y = [7,4,7,8,0,3]

m.plot(x,y) # first linear graph
s.lineplot(x=x,y=y) # second linear graph
m.show()
