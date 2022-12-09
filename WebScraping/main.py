from ScrapeWebsiteDoc import ScrapeWebsite

url="https://www.worldometers.info/coronavirus/"    
country = "S. Korea"

# intialize class object
firstinq = ScrapeWebsite()

# print the results of the inquiry
print(firstinq.scrape_country(url,country))

