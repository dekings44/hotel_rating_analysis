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

url = "https://www.booking.com/searchresults.en-gb.html?label=gen173nr-1DCAEoggI46AdIM1gEaFCIAQGYAQm4ARfIAQzYAQPoAQGIAgGoAgO4Aoq1lpsGwAIB0gIkZjA3N2ZjM2YtMzkzNi00ZDYyLWIzZTQtMTJjZGMyYTlhMWM02AIE4AIB&sid=828d71aca926f8532f0cb1f47b533b81&sb=1&sb_lp=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.en-gb.html%3Flabel%3Dgen173nr-1DCAEoggI46AdIM1gEaFCIAQGYAQm4ARfIAQzYAQPoAQGIAgGoAgO4Aoq1lpsGwAIB0gIkZjA3N2ZjM2YtMzkzNi00ZDYyLWIzZTQtMTJjZGMyYTlhMWM02AIE4AIB%26sid%3D828d71aca926f8532f0cb1f47b533b81%26sb_price_type%3Dtotal%26%26&ss=London%2C+Greater+London%2C+United+Kingdom&is_ski_area=&ssne=Paris&ssne_untouched=Paris&checkin_year=2022&checkin_month=12&checkin_monthday=27&checkout_year=2022&checkout_month=12&checkout_monthday=28&efdco=1&group_adults=2&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1&search_pageview_id=e115a245801601aa&ac_suggestion_list_length=5&ac_suggestion_theme_list_length=0&ac_position=1&ac_langcode=en&ac_click_type=b&ac_meta=GhBlMTE1YTI0NTgwMTYwMWFhIAEoATICZW46BkxvbmRvbkAASgBQAA%3D%3D&dest_id=-2601889&dest_type=city&iata=LON&place_id_lat=51.507393&place_id_lon=-0.127634&search_pageview_id=e115a245801601aa&search_selected=true&ss_raw=London"

header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

#get_page = requests.get(url + str(url) + , headers=header)

get_page = requests.get(url, headers=header)

print(get_page.status_code)

response = get_page.content


print(len(response))

webpage_data = BeautifulSoup(response, 'html5lib')

h_name = webpage_data.find_all('h3', class_='a4225678b2')
hotel_name = [name.text for name in h_name]
print(hotel_name)

h_rating = webpage_data.find_all('div', class_='b5cd09854e d10a6220b4')
hotel_rating = [float(rating.text) for rating in h_rating]
print(hotel_rating)

h_desc = webpage_data.find_all('div', class_='b5cd09854e f0d4d6a2f5 e46e88563a')
hotel_desc = [desc.text for desc in h_desc]
print(hotel_desc)

t_reviews = webpage_data.find_all('div', class_='d8eab2cf7f c90c0a70d3 db63693c62')
total_reviews = [rev.text for rev in t_reviews]
print(total_reviews)

dist_from = webpage_data.find_all('span', class_='cb5ebe3ffb')
dist_from_center = [dist.text for dist in dist_from]
print(dist_from_center)

r_type = webpage_data.find_all('span', class_='df597226dd')
room_type = [room.text for room in r_type]
print(room_type)

b_type = webpage_data.find_all('div', class_='d8eab2cf7f')
bed_type = [bed.text for bed in b_type]
print(bed_type)





# pages = np.arange(0, 615, 25)

# for page in pages: 
  
#   page = requests.get("" + str(page), headers=header)
  
#   soup = BeautifulSoup(response, 'html5lib')
  
#   movie_div = soup.find_all('div', class_='lister-item mode-advanced')
  
#   sleep(randint(2,10))

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