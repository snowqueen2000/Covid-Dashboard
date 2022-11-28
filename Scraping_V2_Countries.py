from bs4 import BeautifulSoup
import requests
import pandas as pd

# here is where our data is coming from
link = 'https://www.worldometers.info/coronavirus/#countries'

# this is the command that requests the data from the specified link above
data = requests.get(link)

#this uses beautiful soup to parse through the data provided
soup = BeautifulSoup(data.text, 'lxml')
print(soup.prettify())

# finding the main three stats on the dashboard
"""
mainStats = soup.find_all('div', {"id": "maincounter-wrap"}) # stats from the main  covid dashboard

mainStatList = [] # list of the stat NUMBERS (must go outside the for loop)
statNameList = [] # list of the corresponding stat NAMES
for stat in mainStats: 
    mainStat = stat.span.text # get text of the span header
    statName = stat.h1.text # get text of the h1 header
    mainStatList.append(mainStat) 
    statNameList.append(statName)
"""
    