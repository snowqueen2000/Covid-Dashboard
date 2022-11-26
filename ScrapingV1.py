from bs4 import BeautifulSoup
import requests
import pandas as pd

link = 'https://www.worldometers.info/coronavirus/#countries'
data = requests.get(link)
soup = BeautifulSoup(data.text, 'lxml')

# finding the main three stats on the dashboard
mainStats = soup.find_all('div', {"id": "maincounter-wrap"})
print(mainStats)



