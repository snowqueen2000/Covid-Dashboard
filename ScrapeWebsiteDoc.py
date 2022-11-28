from bs4 import BeautifulSoup
import requests
import pandas as pd
import json 

class ScrapeWebsite():
    def __init__(self):
        self.website = ""
        self.query_country = ""
        self.total_deaths = None
        self.new_deaths = None

    def scrape_country(self, init_website, init_country):
        self.website = init_website
        self.query_country = init_country

        # Make a GET request to fetch the raw HTML content
        html_content = requests.get(self.website).text

        # Parse HTML code for the entire site
        soup = BeautifulSoup(html_content, "lxml")
        #print(soup.prettify()) # print the parsed data of html

        # pick the id of the table we want to scrape and extract HTML code for that particular table only
        covid_table = soup.find("table", attrs={"id": "main_table_countries_today"})
        
        #the head will form our columns
        head = covid_table.thead.find_all("tr") 
        head #the headers are contained in this HTML code

        headings = []
        for th in head[0].find_all("th"):
            # remove any newlines and extra spaces from left and right
            # print(th.text)
            #headings.append(td.b.text.replace('\n', ' ').strip())
            headings.append(th.text.replace("\n","").strip())

        body = covid_table.tbody.find_all("tr") 
        # body[0] # here is one example of HTML snippet for one row
        
        # declare empty list data that will hold all rows data
        data = []
        for r in range(1,len(body)):
            row = [] # empty lsit to hold one row data
            for tr in body[r].find_all("td"):
                row.append(tr.text.replace("\n","").strip())
                # append row data to row after removing newlines escape and triming unnecesary spaces
            if self.query_country in row:
                data.append(row)
            
        # data contains all the rows excluding header
        # row contains data for one row

        # We can now pass data into a pandas dataframe
        # with headings as the columns
        df = pd.DataFrame(data,columns=headings)
        # df.head(10)

        data = df[df["#"]!=""].reset_index(drop=True)
        # Data points with # value are the countries of the world while the data points with
        # null values for # columns are features like continents totals etc
        
        data = data.drop_duplicates(subset = ["Country,Other"])
        #Reason to drop duplicates : Worldometer reports data for 3 days: today and 2 days back
        #I found out that removing duplicates removes the values for the past two days and keep today's

        # Columns to keep
        cols = ['Country,Other', 'TotalDeaths', 'NewDeaths', 'Deaths/1M pop', 'New Cases/1M pop']
        
        # Extract the columns we are interested in a display the first 5 rows
        data_final = data[cols]
        data_final.to_json(r'covid_data.json')

        with open('covid_data.json', 'r') as filer:
            alldata = json.load(filer)
            counter = 0
            query_country_num = -100

            for i in alldata["Country,Other"]:
                counter_string = str(counter)
                
                if alldata["Country,Other"][i] == self.query_country:
                    self.total_deaths = alldata["TotalDeaths"][i]
                    self.new_deaths = alldata["NewDeaths"][i]
                    self.norm_deaths = alldata['Deaths/1M pop'][i]
                    self.norm_cases = alldata['New Cases/1M pop'][i]
                    query_country_num = counter
                    
                counter += 1
                
            if query_country_num == -100:
                raise LookupError("Failed to find the desired country")
                # print("There was an error searching for that country")
 
            finDF = pd.DataFrame([self.query_country, self.total_deaths, self.new_deaths, self.norm_deaths, self.norm_cases], cols) 
            #return_string = "Data for "  + self.query_country + ":\n" + "Total deaths:" + self.total_deaths + "\n" + "New deaths:" + self.new_deaths + "\n" + "Cases/1m: " + self.norm_deaths + "\n" + "Deaths/1M: " + self.norm_cases
            return finDF