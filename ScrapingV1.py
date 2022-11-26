from bs4 import BeautifulSoup
import requests
import pandas as pd

link = 'https://www.worldometers.info/coronavirus/#countries'
data = requests.get(link)
soup = BeautifulSoup(data.text, 'lxml')

# finding the main three stats on the dashboard
mainStats = soup.find_all('div', {"id": "maincounter-wrap"}) # stats from the main  covid dashboard

mainStatList = [] # list of the stat NUMBERS (must go outside the for loop)
statNameList = [] # list of the corresponding stat NAMES
for stat in mainStats: 
    mainStat = stat.span.text # get text of the span header
    statName = stat.h1.text # get text of the h1 header
    mainStatList.append(mainStat) 
    statNameList.append(statName)
    
print(mainStatList)
print(statNameList)

