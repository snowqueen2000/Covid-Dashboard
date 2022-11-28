from bs4 import BeautifulSoup
import requests
import worldometer as w

print(w.current_world_population())
print(w.days_to_the_end_of_coal())

# This API doesn't have connections to the COVID stats. Therefore we will need to use BS4 to 
# web scrape the covid stats by country! 
