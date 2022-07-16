#Importing necessary libraries

from urllib import response
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import numpy as np
from time import sleep
from random import randint
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# url = 'https://www.tripadvisor.co.uk/Hotels-g191-United_States-Hotels.html'

url = 'https://www.booking.com/searchresults.en-gb.html?label=gen173nr-1FCAEoggI46AdIM1gEaFCIAQGYAQm4ARfIAQzYAQHoAQH4AQuIAgGoAgO4AtLB_JEGwAIB0gIkZDg0Y2M3MjYtZjc0Yy00OTI0LWFmNTEtNzFhOTc3MTY0ZjBk2AIG4AIB&sid=828d71aca926f8532f0cb1f47b533b81&aid=304142&ss=London&ssne=London&ssne_untouched=London&lang=en-gb&sb=1&src_elem=sb&src=searchresults&dest_id=-2601889&dest_type=city&checkin=2022-07-16&checkout=2022-07-17&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure&offset='

header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

get_page = requests.get(url + str(url) + , headers=header)

print(get_page.status_code)

response = get_page.content

# print(len(response))

webpage_data = BeautifulSoup(response, 'html5lib')



pages = np.arange(0, 615, 25)

for page in pages: 
  
  page = requests.get("https://www.booking.com/searchresults.en-gb.html?label=gen173nr-1FCAEoggI46AdIM1gEaFCIAQGYAQm4ARfIAQzYAQHoAQH4AQuIAgGoAgO4AtLB_JEGwAIB0gIkZDg0Y2M3MjYtZjc0Yy00OTI0LWFmNTEtNzFhOTc3MTY0ZjBk2AIG4AIB&sid=828d71aca926f8532f0cb1f47b533b81&aid=304142&ss=London&ssne=London&ssne_untouched=London&lang=en-gb&sb=1&src_elem=sb&src=searchresults&dest_id=-2601889&dest_type=city&checkin=2022-07-16&checkout=2022-07-17&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure&offset=" + str(page), headers=header)
  
  soup = BeautifulSoup(response, 'html5lib')
  
  movie_div = soup.find_all('div', class_='lister-item mode-advanced')
  
  sleep(randint(2,10))

# print(webpage_data)

# hotel = []
# for name in webpage_data.findAll('div', {'data-testid' : 'title'}):
#     hotel.append(name.text)
#     print(hotel)

# pizza = webpage_data.find_all('a', {'class' : 'css-1m051bw'})

# pizzaStores = [name.text for name in webpage_data.findAll('div', {'data-testid' : 'title'})]

# # print(pizzaStores)

# pizzaLoc = [loc.text.strip('Show on map') for loc in webpage_data.findAll('span', {'class' : 'af1ddfc958 eba89149fb'})]

# # print(pizzaLoc)

# pizza_status = [stat.text.strip() for stat in webpage_data.findAll('div', {'class' : '_9c5f726ff _192b3a196 f1cbb919ef'})]

# # print(pizza_status)

# pizza_rating = [rating.text.strip() for rating in webpage_data.findAll('div', {'class' : '_9c5f726ff bd528f9ea6'})]

# # print(pizza_rating)

# room_rev = [reviews.text.strip(' reviews') for reviews in webpage_data.findAll('div', {'class' : '_4abc4c3d5 _1e6021d2f _6e869d6e0'})]

# # print(room_rev)

# room_type = [roomtype.text.strip() for roomtype in webpage_data.find_all('span', {'class' : '_c5d12bf22'})]

# print(room_type)

# room_typ = [roomtype.text.strip() for roomtype in webpage_data.findAll('span', {'class' : '_c5d12bf22'})]

# print(room_typ)