# This entrypoint file to be used in development. Start by reading README.md
#import time_series_visualizer
#from unittest import main

# Test your function by calling it here
#time_series_visualizer.draw_line_plot()
#time_series_visualizer.draw_bar_plot()
#time_series_visualizer.draw_box_plot()

# Run unit tests automatically
#main(module='test_module', exit=False)

#----my code starts here----
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import seaborn as sns

#read csv, parse dates, set index to date column
df = pd.read_csv("fcc-forum-pageviews.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.set_index("date")

#clean data, removing upper 2.5% quantile and lower 2.5% quantile
df = df[(df["value"]<= df["value"].quantile(0.975))
       & (df["value"] >= df["value"].quantile(0.025))]

#line plot
fig, ax = plt.subplots(figsize=(20,10)) 
line_plot = plt.plot(df.index, df["value"])
plt.xlabel("Date")
plt.ylabel("Page Views")
plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
fig.savefig('line_plot.png')

#bar plot data
df_bar = df
df_bar["year"] = df_bar.index.year
df_bar["month"] = df_bar.index.month_name()
df_bar = df_bar.groupby(["year", "month"], as_index=False, sort=False)["value"].mean()
df_pivot = df_bar.pivot("year", "month", "value")
#months = ["January", "February", "March", "April", "May", "June", "July", "August", "SEpt"]
print (df_pivot.head(24))

#bar plot
fig,ax = plt.subplots()
ax = df_pivot.plot(kind='bar', figsize = (16,9), xlabel = 'Year', ylabel = 'Average Page Views')
#ax = df_bar.plot.bar(rot = 0)
#df_pivot.plot(kind = "bar")
#plt.xlabel("Years")
#plt.ylabel("Average Page Views")
#plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
#plt.legend()
fig.savefig('bar_plot.png')