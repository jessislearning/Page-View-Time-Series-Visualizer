# Page View Time Series Visualizer

This is the boilerplate for the Page View Time Series Visualizer project. Instructions for building your project can be found at https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/page-view-time-series-visualizer


The file fcc-forum-pageview.csv contains a time series data of the freeCodeCamp forum page views.
From the CSV file, we use matplotlib and seaborn libraries to:

1. Produce a line plot of the Daily freeCodeCamp Forum Page Views 5/2016-12/2019
2. Create a bar plot of the average daily views each month, for every year available.
3. Create a box plot showing the trend of page views (views by year), and a second box plot showing the seasonality of page views (views by month)

In order to do the tasks above, the data was:
- imported from the CSV file
- dates were parsed
- dates were used as the index
- data was cleaned to remove the upper and lower 2.5 quantiles 

Additional formatting were performed to:
- ensure that months were in order (instead of alphabetical)


Notes: I was encountering a numpy Attribute Error. The boilerplate version that we forked was using seaborn 0.9.0. To fix the issue, I updated the "requirements.txt" to use seaborn 0.13.2
and updated seaborn in gitpod.

I was aided by the freeCodeCamp forum:
https://forum.freecodecamp.org/t/boxplot-error-for-page-view-time-series-analyzer/683684

prior to forum consultation, I used "monkey patches" as suggested here:
https://stackoverflow.com/questions/74844262/how-can-i-solve-error-module-numpy-has-no-attribute-float-in-python