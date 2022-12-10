from ScrapeWebsite import ScrapeWebsite
from bokeh.plotting import figure, show
import json

# define the URL
url="https://www.worldometers.info/coronavirus/"

# define desired country to get data on
country = "Japan"

# intialize class object
firstinq = ScrapeWebsite()

# print the results of the inquiry
print(firstinq.scrape_country(url,country))
  
# Opening JSON file
# f = open('covid_data.json')
  
# returns JSON object as 
# a dictionary
# data = json.load(f)
  
# a = data.values()

# print(a)