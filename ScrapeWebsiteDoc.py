from bs4 import BeautifulSoup
import requests
import pandas as pd
import json 
import os.path
from os import path
import time

class ScrapeWebsite():
    def __init__(self):
        self.website = ""
        self.query_country = ""
        self.total_deaths = None
        self.new_deaths = None

    def scrape_country(self, init_website, init_country):
        # intialize the class variables passed in
        self.website = init_website
        self.query_country = init_country

        # Make a GET request to fetch the raw HTML content
        html_content = requests.get(self.website).text

        # Parse HTML code for the entire site
        soup = BeautifulSoup(html_content, "lxml")

        # get data from a specific html table on the site
        covid_table = soup.find("table", attrs={"id": "main_table_countries_today"})

        # get data on headings
        head = covid_table.thead.find_all("tr") 

        # empty list 
        headings = []
        for th in head[0].find_all("th"):
            # get list of headings
            headings.append(th.text.replace("\n","").strip())

        # get all row data
        body = covid_table.tbody.find_all("tr") 
        
        # declare empty list
        data = []

        # loop through the columns
        for r in range(1,len(body)):
            row = [] # empty lsit to hold one row data
        
            # loop through the rows
            for tr in body[r].find_all("td"):
                # append next piece of data onto row
                row.append(tr.text.replace("\n","").strip())

            # if there is a matching data point then save data and break out of loops
            if self.query_country in row:
                data.append(row)
                break

        # pass data into a pandas dataframe
        df = pd.DataFrame(data,columns=headings)
        
        # only get the country data, they are the ones with a #
        data = df[df["#"]!=""].reset_index(drop=True)
        
        # drop any duplicates 
        data = data.drop_duplicates(subset = ["Country,Other"])

        # Define which columns to keep
        cols = ['Country,Other', 'TotalDeaths', 'NewDeaths', 'Deaths/1M pop', 'New Cases/1M pop']

        # Extract the columns we are interested in
        data_final = data[cols]

        # if the data file doesnt exist, just put all the current data in a new file
        if not path.exists('covid_data.json'):
            print("no file exists with data.. creating..")
            data_final.to_json(r'covid_data.json')
        
        # if the file does exist, add in all the current data into the existing data
        else:
            # retrieve the current .json data
            with open('covid_data.json', 'r') as current_file:
                thisone = json.load(current_file)
                input_dict = thisone

            # check to make sure this countries data isnt already in the .json file
            if not self.query_country in thisone["Country,Other"].values():
                # get the length of the dictionary
                num_data_points = len(input_dict["Country,Other"])

                # add new data points to the python dictionary
                for datapoint in data_final:
                    input_dict[datapoint][num_data_points] = data_final[datapoint][0]

                # convert the dictionary to dataframe and save it in json file
                input_df = pd.DataFrame.from_dict(input_dict)
                input_df.to_json(r'covid_data.json')
        
        # open that file back up
        with open('covid_data.json', 'r') as current_file:
            # get the data in file
            alldata = json.load(current_file)

            # initialize some variables
            counter = 0
            query_country_num = -100

            # parse through all countries in .json file
            for i in alldata["Country,Other"]:
                # save what data point we are currently on
                counter_string = str(counter)

                # check to see if the current data is that of the desired country 
                if alldata["Country,Other"][i] == self.query_country:

                    # save all of the data to the class variables
                    self.total_deaths = alldata["TotalDeaths"][i]
                    self.new_deaths = alldata["NewDeaths"][i]
                    self.norm_deaths = alldata['Deaths/1M pop'][i]
                    self.norm_cases = alldata['New Cases/1M pop'][i]
                    query_country_num = counter
                counter += 1
            
            # if this variable didnt get  overwritten then there was a problem
            if query_country_num == -100:
                print("There was an error searching for that country")

            # prepare return line
            # return_string = str(data_final.to_dict())
            return_string = "Data for "  + self.query_country + ":\n" + "Total deaths:" + self.total_deaths + "\n" + "New deaths:" + self.new_deaths + "\n" + "Cases/1m: " + self.norm_deaths + "\n" + "Deaths/1M: " + self.norm_cases
            return return_string
    
    