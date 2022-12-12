from ScrapeWebsite import ScrapeWebsite
from DataPlotting import PlotData

# define the URL
url="https://www.worldometers.info/coronavirus/"

# define desired country to get data on
countries = ["USA", "India", "S. Korea", "Japan", "Russia", "Australia", "China"]

# intialize class object
firstinq = ScrapeWebsite()

# print the results of the inquiry
for country in countries:
    print(firstinq.scrape_country(url,country))

# open html and show data
PlotData()
