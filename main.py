
from ScrapeWebsiteDoc import ScrapeWebsite

#Lets define the URL

url="https://www.worldometers.info/coronavirus/"    
country = "S. Korea"

firstinq = ScrapeWebsite()
print(firstinq.scrape_country(url,country))


# alldeaths = alldata["TotalDeaths"][str(query_country_num)]

# newdeaths = alldata["NewDeaths"][query_country_num]
# print("The number of deaths for " + query_country + " is " + str(alldeaths))
# print("The number of new deaths for " + query_country + " is " + str(newdeaths))

# if "0" in alldata["Country,Other"]:
#     print("%s is found in JSON data" %"0")
#     print("The value of", "0","is", alldata["Country,Other"]["0"])
# else:
#     # Print the message if the value does not exist
#     print("%s is not found in JSON data" %"0")
