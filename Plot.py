from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, TableColumn, DataTable
from bokeh.models.widgets import DataTable, DateFormatter, TableColumn
from bokeh.io import show
import pandas as pd
from Main import cD

print(cD) # cD is the data frame exported from the main script!! We can manipulate it and graph it here 

# read in country csv
# SouthKorea = pd.read_csv('South Korea.txt')
# DF.iat[] is a pandas command to access the data at an index of ... 
# if you want to use the row/col name use DF.at[]
# in this case col 0 is the name of the stats, col 1 are the stats
# rows 0-4 are the things we scraped from the table in ScrapeWebsiteDoc.py
#Country = SouthKorea.iat[0,1] # this line gets the name of country based on index
#NewDeath = SouthKorea.iat[2, 1] # this line gets new deaths based on index 
#print(Country)
#print(NewDeath)

#Columns = [TableColumn(field=Ci, title=Ci) for Ci in SouthKorea.columns] # bokeh columns
#data_table = DataTable(columns=Columns, source=ColumnDataSource(SouthKorea)) # bokeh table

#show(data_table)

# this is just messing around making a simple line graph 
"""
output_file('testing.html')

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [1, 0, -1, 0, 1, 0, -1, 0, 1, 0]

p = figure(
    title = 'Beep Boop Video Tutorial',
    x_axis_label = 'X-Axis', 
    y_axis_label = 'Y-Axis',  
)

# render glyph
p.line(x, y, legend = 'Test!', line_width = 3)

# show the plot! 
show(p)
"""
