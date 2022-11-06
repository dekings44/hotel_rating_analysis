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
def hotel_data(url, file_name):

  header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

  page = requests.get(url, headers=header)

  #get_page = requests.get(url, headers=header)

  #print(get_page.status_code)

  response = page.content


  #print(len(response))

  webpage_data = BeautifulSoup(response, 'html5lib')
  sleep(randint(2,6))

  h_name = webpage_data.find_all('h3', class_='a4225678b2')
  hotel_name = [name.text if h_name else '' for name in h_name ]
  print(len(hotel_name))

  h_rating = webpage_data.find_all('div', class_='b5cd09854e d10a6220b4')
  hotel_rating = [float(rating.text) if h_rating else '' for rating in h_rating ]
  print(len(hotel_rating))

  h_desc = webpage_data.find_all('div', class_='b5cd09854e f0d4d6a2f5 e46e88563a')
  hotel_desc = [desc.text if h_desc else '' for desc in h_desc ]
  print(len(hotel_desc))

  t_reviews = webpage_data.find_all('div', class_='d8eab2cf7f c90c0a70d3 db63693c62')
  total_reviews = [rev.text if t_reviews else '' for rev in t_reviews ]
  print(len(total_reviews))

  # dist_from = webpage_data.find_all('span', class_='cb5ebe3ffb')
  # dist_from_center = [dist.text if dist_from else '' for dist in dist_from ]
  # print(len(dist_from_center))

  r_type = webpage_data.find_all('span', class_='df597226dd')
  room_type = [room.text if r_type else '' for room in r_type ]
  print(len(room_type))

  # b_type = webpage_data.find_all('div', class_='d8eab2cf7f')
  # bed_type = [bed.text if b_type else '' for bed in b_type ]
  # print(len(bed_type))

  r_price = webpage_data.find_all('span', {'data-testid': 'price-and-discounted-price'})
  room_price = [price.text if r_price != ' ' else '' for price in r_price ]
  print(len(room_price))
  print(room_price)

  my_data = {
  'name': hotel_name,
  'rating': hotel_rating,
  'rating_desciption': hotel_desc,
  'total_reviews': total_reviews,
  'room_type': room_type,
  'room_price': room_price
  }

  h_data = pd.DataFrame(my_data)
  h_data.transpose()
  h_data.to_csv(file_name, index=False,header=True, encoding='utf-8')



hotel_data('https://www.booking.com/searchresults.en-gb.html?label=gen173nr-1DCAEoggI46AdIM1gEaFCIAQGYAQm4ARfIAQzYAQPoAQGIAgGoAgO4AouloJsGwAIB0gIkMGRmMWU0N2EtZjg5YS00NmIzLWE2NTQtNmJmNGM4ZGVhMjM02AIE4AIB&sid=828d71aca926f8532f0cb1f47b533b81&sb=1&sb_lp=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.en-gb.html%3Flabel%3Dgen173nr-1DCAEoggI46AdIM1gEaFCIAQGYAQm4ARfIAQzYAQPoAQGIAgGoAgO4AouloJsGwAIB0gIkMGRmMWU0N2EtZjg5YS00NmIzLWE2NTQtNmJmNGM4ZGVhMjM02AIE4AIB%26sid%3D828d71aca926f8532f0cb1f47b533b81%26sb_price_type%3Dtotal%26%26&ss=London&is_ski_area=0&ssne=London&ssne_untouched=London&dest_id=-2601889&dest_type=city&checkin_year=2022&checkin_month=12&checkin_monthday=24&checkout_year=2022&checkout_month=12&checkout_monthday=25&efdco=1&group_adults=2&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1', 'hotel_data1.csv')


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