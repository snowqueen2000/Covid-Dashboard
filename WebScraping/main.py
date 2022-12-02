from ScrapeWebsiteDoc import ScrapeWebsite

<<<<<<< HEAD:main.py
# define the URL
url="https://www.worldometers.info/coronavirus/"

# define desired country to get data on
country = "Brazil"
=======
url="https://www.worldometers.info/coronavirus/"    
country = "S. Korea"
>>>>>>> af7c556036d362a9d43ec7396a695b21d28200ad:WebScraping/main.py

# intialize class object
firstinq = ScrapeWebsite()

# print the results of the inquiry
print(firstinq.scrape_country(url,country))

