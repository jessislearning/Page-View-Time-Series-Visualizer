import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.set_index("date")

# Clean data
df = df[(df["value"]<= df["value"].quantile(0.975))
       & df["value"] >= df["value"].quantile(0.025)]


def draw_line_plot():
    fig, ax = plt.subplots(figsize=(20,10)) 
    line_plot = plt.plot(df.index, df["value"])
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    #df_bar = None

    df_bar = df
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month
    df_group = df_bar.groupby(["year", "month"], as_index=False, sort=False)["value"].mean()
    df_pivot = df_group.pivot("year", "month", "value").fillna(0)
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    df_pivot.columns = months
    
    # Draw bar plot
    ax = df_pivot.plot(kind='bar', figsize = (8,8), xlabel='Years', ylabel='Average Page Views')
    fig = ax.get_figure()
    plt.legend(title="Months")


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
