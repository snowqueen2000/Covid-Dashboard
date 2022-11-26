from bs4 import BeautifulSoup
import requests
import pandas as pd

link = 'https://www.worldometers.info/coronavirus/'
data = requests.get(link)
soup = BeautifulSoup(data.text, 'lxml')
print(soup)




