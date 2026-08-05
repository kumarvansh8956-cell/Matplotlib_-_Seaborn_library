import matplotlib.pyplot as ma
import seaborn as s
import pandas as p

df = p.read_csv("car details v4.csv")
print(df.columns)

Max = df.groupby("Make")["Price"].sum().sort_values(ascending= False).head(3)
print(Max)
Mak_data =df.loc[df["Make"].isin(Max.index)]
print(Mak_data)


s.violinplot(data=Mak_data, x="Make", y="Price", palette="Set3")
ma.show()



"""

MOST COMMON ONE

| Palette        | Description                           |
| -------------- | ------------------------------------- |
| `"deep"`       | Default Seaborn colors                |
| `"muted"`      | Soft colors                           |
| `"bright"`     | Bright, vibrant colors                |
| `"pastel"`     | Light pastel colors                   |
| `"dark"`       | Dark shades                           |
| `"colorblind"` | Colorblind-friendly colors            |
| `"Set1"`       | Strong categorical colors             |
| `"Set2"`       | Soft categorical colors               |
| `"Set3"`       | Many light colors                     |
| `"Paired"`     | Paired contrasting colors             |
| `"husl"`       | Evenly spaced vibrant colors          |
| `"coolwarm"`   | Blue → Red gradient (continuous data) |
| `"viridis"`    | Purple → Green gradient               |
| `"magma"`      | Black → Orange gradient               |



"""