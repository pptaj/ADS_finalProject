from bs4 import BeautifulSoup
import mechanicalsoup
import pandas as pd

            
data = pd.read_csv('https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2016-01.csv');

data.head()
