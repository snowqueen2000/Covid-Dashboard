from ScrapeWebsite import ScrapeWebsite

# define the URL
url="https://www.worldometers.info/coronavirus/"

# define desired country to get data on
country = "Mexico"

# intialize class object
firstinq = ScrapeWebsite()

# print the results of the inquiry
print(firstinq.scrape_country(url,country))

