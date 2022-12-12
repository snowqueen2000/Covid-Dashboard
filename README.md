# Covid-Dashboard
Final Project for MEEN 6250 Programming for Engineers

INSTRUCTIONS TO RUN CODE:

1. In git bash use the command "git clone https://github.com/snowqueen2000/Covid-Dashboard.git"
2. Open main.py 
3. Enter a list of countries you would like to see Covid data for
4. Run main.py, it calls the function ScrapeWebsite.py to retrieve current data on the website https://www.worldometers.info/coronavirus/ , then, the main.py calls a DataPlotting function that redirects the user to an html page with the data displayed.

Part 1: Data Scraping 

Our data is collected using the webpage https://www.worldometers.info/coronavirus/ with daily updates on totals. When main.py is run, ScrapeWebsite.py is called which imports Beautifulsoup to parse data from HTML documents. Using a user-provided country name, and the url listed above, ScrapeWebsite.py runs scrape_country to extract the data from worldometer and then parses through the information from a table to get desired information.

Once ScrapeWebsite initializes, it will go on to create a new file, covid_data.json, to store each set of data. Our .json file is organized so that it is only created once, and each time a new country is called in the main script, covid_data.json will append the new set. If a user decides to re-run main.py using an already listed country, there is no new data added to the .json file. 

Part 2: Data Display 

We have created a function DataPlotting.py that converts the data collected in Part 1 into user-friendly graphs. We begin by converting the data contained with covid_data.json to a DataFrame using Pandas. 

In order for bokeh to properly read the data within our DataFrame, we removed all commas from each column. 

Once our data was correctely formatted, we turned our DataGrame into a graph. Each graph takes a country contained with our JSON file and displays each of its stats in a bar graph. 

