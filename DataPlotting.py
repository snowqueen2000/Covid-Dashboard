from bokeh.plotting import figure, show
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
      
# deletes all commas bc it gets mad if you don't      
data = data.replace(',','', regex=True)

# creating an int list with the totalDeaths data
top = [int(x) for x in data['TotalDeaths']]
countries = list(data['Country,Other'])
sorted_countries = sorted(countries, key = lambda x: top[countries.index(x)]) # sorts from low to high

p = figure(x_range=sorted_countries, height=250, title="COVID Deaths Per Country", # defining figure dimensions
           toolbar_location=None, tools="") 

# plotting the graph
p.vbar(x = countries, top = top, width=0.9) 
show(p)