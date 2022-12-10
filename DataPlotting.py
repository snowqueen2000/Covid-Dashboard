from bokeh.plotting import figure, show
"""
# prepare some data
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

# create a new plot with a title and axis labels
p = figure(title="Simple line example", x_axis_label='x', y_axis_label='y')

# add a line renderer with legend and line thickness to the plot
p.line(x, y, legend_label="Temp.", line_width=2)

# show the results
show(p)
"""

import json
  
# Opening JSON file
f = open('covid_data.json')
  
# returns JSON object as a dictionary
data = json.load(f)
  
# Iterating through the json list
for i in data['Country,Other']:
    print(i)
  
# Closing file
f.close()