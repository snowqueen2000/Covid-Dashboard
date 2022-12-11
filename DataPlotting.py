def PlotData():
    # import a bunch of stuff from bokeh
    from bokeh.io import output_file, show
    from bokeh.layouts import gridplot
    from bokeh.plotting import figure
    from bokeh.transform import factor_cmap
    from bokeh.models import Div
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

    # repalce all blanks with 0 bc it gets mad if you don't      
    data = data.replace('','0', regex=True)

    # creating an int list with the totalDeaths data
    totalDeaths = [int(x) for x in data['TotalDeaths']]
    # creating an int list with the totalDeaths per 1M data
    totalDeaths_1M = [int(x) for x in data['Deaths/1M pop']]
    # creating an int list with the newlDeaths
    newDeaths = [int(x) for x in data['NewDeaths']]
    # creating an int list with the newCases per 1M data
    newCases_1M = [int(x) for x in data['New Cases/1M pop']]
    # creating a string list with the names of each country 
    countries = list(data['Country,Other'])
    # sort the countries in order of resepcted data
    sorted_countries_totalDeaths = sorted(countries, key = lambda x: totalDeaths[countries.index(x)]) # sorts from low to high for total deaths
    sorted_countries_totalDeaths_1M = sorted(countries, key = lambda x: totalDeaths_1M[countries.index(x)]) # sorts from low to high for deaths per 1M
    sorted_countries_newDeaths = sorted(countries, key = lambda x: newDeaths[countries.index(x)]) # sorts from low to high for newDeaths
    sorted_countries_newCases_1M = sorted(countries, key = lambda x: newCases_1M[countries.index(x)]) # sorts from low to high for newDeaths
    # defining figure dimensions for plot 1 (p1)
    p1 = figure(x_range=sorted_countries_totalDeaths, title="COVID Deaths Per Country", 
            toolbar_location=None, tools="") 
    p1.vbar(x = countries, top = totalDeaths, width=0.9,color="red") 

    # defining figure dimensions for plot 2 (p2)
    p2 = figure(x_range=sorted_countries_totalDeaths_1M, title="COVID Deaths Per 1M Population per Country", 
            toolbar_location=None, tools="") 
    p2.vbar(x = countries, top = totalDeaths_1M, width=0.9,color="orange") 

    # defining figure dimensions for plot 3 (p3)
    p3 = figure(x_range=sorted_countries_newDeaths, title="New Deaths per Country", 
            toolbar_location=None, tools="") 
    p3.vbar(x = countries, top = newDeaths, width=0.9,color="blue") 

    # defining figure dimensions for plot 4 (p4)
    p4 = figure(x_range=sorted_countries_newCases_1M, title="New Cases per 1M Population per Country", 
            toolbar_location=None, tools="") 
    p4.vbar(x = countries, top = newCases_1M, width=0.9,color="purple") 

    p_all = gridplot([p1,p2,p3,p4], ncols=2, width=500, height=250)


    # div = Div(text="ME EN 6250 Final Project \n Audrey Pohl Ben Silberman Dallen Unruh ", style={'font-size': '200%', 'color': 'blue'})
    
    show(p_all)

