# Covid-Dashboard
Final Project for MEEN 6250 Programming for Engineers

INSTRUCTIONS TO RUN CODE:

1. Open main.py 
2. Enter the name of a country you wish to find data for
3. main.py calls the function ScrapeWebsite.py, however the user does not need to be concerned with this function. 

Part 1: Data Scraping 

Our data is collected using the webpage https://www.worldometers.info/coronavirus/ with daily updates on totals. When main.py is run, ScrapeWebsite.py is called which imports Beautifulsoup to parse data from HTML documents. Using a user-provided country name, and the url listed above, ScrapeWebsite.py runs scrape_country to extract the desired data. 

Once ScrapeWebsite initializes, it will go on to create a new file, covid_data.json, to store each set of data. Our .json file is organized so that it is only created once, and each time a new country is called in the main script, covid_data.json will append the new set. If a user decides to re-run main.py using an already listed country, there is no new data added to the .json file. 

https://github.com/matheusfelipeog/worldometer