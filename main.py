from ScrapeWebsite import ScrapeWebsite
from bokeh.plotting import figure, show
import json
from DataPlotting import PlotData

# define the URL
url="https://www.worldometers.info/coronavirus/"

# define desired country to get data on
countries = ["USA", "India", "S. Korea", "Japan", "Russia"]

# intialize class object
firstinq = ScrapeWebsite()

# print the results of the inquiry
for country in countries:
    print(firstinq.scrape_country(url,country))
  
PlotData()
