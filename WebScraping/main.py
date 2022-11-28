from ScrapeWebsiteDoc import ScrapeWebsite

url="https://www.worldometers.info/coronavirus/"    
country = "S. Korea"

firstinq = ScrapeWebsite()
print(firstinq.scrape_country(url,country))

# print("this is the new deaths " + firstinq.new_deaths)
