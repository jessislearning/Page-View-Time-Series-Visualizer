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

df = pd.read_csv("fcc-forum-pageviews.csv").set_index("date")
df = df[(df["value"]<= df["value"].quantile(0.975))]

fig, ax = plt.subplots(figsize=(20,10)) 
line_plot = plt.plot(df.index, df["value"])
plt.xlabel("Date")
plt.ylabel("Page Views")
plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
fig.savefig('line_plot.png')

#print(plt.show)
