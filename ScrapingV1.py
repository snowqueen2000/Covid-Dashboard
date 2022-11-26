from bs4 import BeautifulSoup
import requests
import pandas as pd

link = 'https://www.worldometers.info/coronavirus/#countries'
data = requests.get(link)
soup = BeautifulSoup(data.text, 'lxml')

# finding the main three stats on the dashboard
mainStats = soup.find_all('div', {"id": "maincounter-wrap"})

mainStatList = []
statNameList = []
for stat in mainStats:
    mainStat = stat.span.text
    statName = stat.h1.text
    mainStatList.append(mainStat)
    statNameList.append(statName)

"""""
statNameList = []
for name in statNames:
    statName = name.h1.text
    statNameList.append(statName)
"""""
    
print(mainStatList)
print(statNameList)

