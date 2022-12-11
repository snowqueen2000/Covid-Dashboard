def PlotData():
    from bokeh.io import output_file, show
    from bokeh.layouts import column
    from bokeh.plotting import figure
    import json
    import pandas as pd
    from bokeh.transform import factor_cmap
    #from bokeh.palettes import Magma

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
    totalDeaths = [int(x) for x in data['TotalDeaths']]
    # creating an int list with the totalDeaths per 1M data
    totalDeaths_1M = [int(x) for x in data['Deaths/1M pop']]
    # creating a string list with the names of each country 
    countries = list(data['Country,Other'])
    # sort the countries in order of resepcted data
    sorted_countries_deaths = sorted(countries, key = lambda x: totalDeaths[countries.index(x)]) # sorts from low to high for total deaths
    sorted_countries_deaths1M = sorted(countries, key = lambda x: totalDeaths_1M[countries.index(x)]) # sorts from low to high for deaths per 1M

    p1 = figure(x_range=sorted_countries_deaths, height=250, title="COVID Deaths Per Country", # defining figure dimensions for plot 1 (p1)
            toolbar_location=None, tools="") 

    p1.vbar(x = countries, top = totalDeaths, width=0.9) 

    p2 = figure(x_range=sorted_countries_deaths1M, height=250, title="COVID Deaths Per 1M Population per Country", # defining figure dimensions for plot 2 (p2)
            toolbar_location=None, tools="") 
    p2.vbar(x = countries, top = totalDeaths_1M, width=0.9) 

    p_all = column(p1, p2)

    show(p_all)

