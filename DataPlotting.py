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
import pandas as pd

# Opening JSON file
f = open('covid_data.json')
  
# returns JSON object as a dictionary
data = json.load(f)
data = pd.DataFrame(data)
print(data) 
  
# Closing file
f.close()

'''
p = figure(
    title = 'Beep Boop Video Tutorial',
    x_axis_label = 'X-Axis', 
    y_axis_label = 'Y-Axis',  
)

# render glyph
p.line(x, y, legend = 'Test!', line_width = 3)

# graphing! 
data.plot_bokeh(
    kind = 'bar',
    x = 'Country,Other',
    y = ['TotalDeaths', 'Deaths/1M pop'],
    xlabel = 'Country',
    ylabel = 'Deaths',
    title = 'Deaths per Country'
)

# show the plot! 
show(p)
'''

from bokeh.plotting import figure, output_file, show
      
# x-coordinates of the top edges
#top = data['TotalDeaths']
#top = data['TotalDeaths']
#print(type(list(top)))
#top = [int(x) for x in top]
#top = list(map(int, list(data['TotalDeaths'])))
#print(type(top[0]))
#print(top)

top = [689998, 1106378, 19952, 330525, 116422, 11906, 5235, 9046, 51512]

p = figure(x_range=data['Country,Other'], height=250, title="COVID Deaths Per Country",
           toolbar_location=None, tools="")

# plotting the graph
p.vbar(x = list(data['Country,Other']), top = top, width=0.9)
  
# displaying the model
show(p)