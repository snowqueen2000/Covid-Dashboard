def PlotData():
    # import a bunch of stuff from bokeh
    from bokeh.io import output_file, show
    from bokeh.layouts import gridplot, column
    from bokeh.plotting import figure
    from bokeh.transform import factor_cmap
    from bokeh.models import Div
    from bokeh.models.widgets import Tabs, Panel
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
    totalDeaths = [float(x) for x in data['TotalDeaths']]
    # creating an int list with the totalDeaths per 1M data
    totalDeaths_1M = [float(x) for x in data['Deaths/1M pop']]
    # creating an int list with the newlDeaths
    newDeaths = [float(x) for x in data['NewDeaths']]
    # creating an int list with the newCases per 1M data
    newCases_1M = [float(x) for x in data['New Cases/1M pop']]
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
    tab1 = Panel(child=p1, title="Total Deaths")

    # defining figure dimensions for plot 2 (p2)
    p2 = figure(x_range=sorted_countries_totalDeaths_1M, title="COVID Deaths Per 1M Population per Country", 
            toolbar_location=None, tools="") 
    p2.vbar(x = countries, top = totalDeaths_1M, width=0.9,color="orange")
    tab2 = Panel(child=p2, title="Total Deaths/1M")

    # defining figure dimensions for plot 3 (p3)
    p3 = figure(x_range=sorted_countries_newDeaths, title="New Deaths per Country", 
            toolbar_location=None, tools="") 
    p3.vbar(x = countries, top = newDeaths, width=0.9,color="blue") 
    tab3 = Panel(child=p3, title="New Deaths")

    # defining figure dimensions for plot 4 (p4)
    p4 = figure(x_range=sorted_countries_newCases_1M, title="New Cases per 1M Population per Country", 
            toolbar_location=None, tools="") 
    p4.vbar(x = countries, top = newCases_1M, width=0.9,color="purple") 
    tab4 = Panel(child=p4, title="New Cases/1M")

    tabs = Tabs(tabs=[tab1,tab2,tab3,tab4])

#     p_all = gridplot([p1,p2,p3,p4], ncols=2, width=500, height=250)

    div = Div(text="ME EN 6250 Final Project", styles={'font-size': '200%', 'color': 'black'})
    div2 = Div(text="By Audrey Pohl, Ben Silberman, and Dallen Unruh ", styles={'font-size': '180%', 'color': 'blue'})

#     show(column(div,div2,p_all))
    show(column(div,div2,tabs))

