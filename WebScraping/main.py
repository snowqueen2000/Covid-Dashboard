from ScrapeWebsiteDoc import ScrapeWebsite

url="https://www.worldometers.info/coronavirus/"    
country = "Brazil"

# intialize class object
firstinq = ScrapeWebsite()

# print the results of the inquiry
print(firstinq.scrape_country(url,country))
# shouldn't running this create a text file in our directory that has the info for that country?? 
