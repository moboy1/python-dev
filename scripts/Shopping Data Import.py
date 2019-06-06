#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse

#import urllib.request
#r = urllib.request.urlopen(url)
#data = r.read()

#from selenium import webdriver
#driver = webdriver.Chrome('C:/Users/mgaye_ext/node_modules/chromedriver/lib/chromedriver/chromedriver.exe')
#r = driver.get(url)
#data = driver.page_source


url="https://groceries.morrisons.com/browse/frozen-104162/ice-cream-168439"
parsed_url=urlparse(url)
url_home = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_url)[:-1]
r = requests.get(url)
data = r.text
html=BeautifulSoup(data, 'html')
product_listings=html.find_all("li", {"class": "fops-item"})

df=pd.DataFrame(columns=('product_image', 'product_description', 'product_on_offer', 'product_offer', 'product_weight', 'product_price', 'product_old_price', 'product_unit_price'))

i=0
for product_listing in product_listings:
#    if i<70: 
    product_offer=np.nan
    if product_listing.find("h4", class_="fop-title"):
        product_description=product_listing.find("h4", class_="fop-title").text
    if product_listing.find("img", class_="fop-img"):
        product_image=url_home + product_listing.find("img", class_="fop-img").attrs["src"]
    if product_listing.find("span", class_="fop-catch-weight"):
        product_weight=product_listing.find("span", class_="fop-catch-weight").text
    if product_listing.find("span", class_="fop-price"):
        product_price=product_listing.find("span", class_="fop-price").text
    if product_listing.find("span", class_="fop-old-price"):
        product_old_price=product_listing.find("span", class_="fop-old-price").text
    if product_listing.find("span", class_="fop-unit-price"):
        product_unit_price=product_listing.find("span", class_="fop-unit-price").text
    if product_listing.find("a", class_="fop-row-promo promotion-offer"):
        product_offer=product_listing.find("a", class_="fop-row-promo promotion-offer").span.text
    if pd.isna(product_offer):
        product_on_offer="N"
    else:
        product_on_offer="Y"

    df.loc[i] = [product_image, product_description, product_on_offer, product_offer, product_weight, product_price, product_old_price, product_unit_price]
    product_description, product_image, product_weight, product_price, product_old_price, product_unit_price, product_offer, product_on_offer = [np.nan] * 8
    
    i+=1
    
df=df.dropna(subset=['product_image', 'product_description', 'product_offer', 'product_weight', 'product_price', 'product_old_price', 'product_unit_price'], how='all')
df.to_csv("C:/Users/mgaye_ext/Work/training/python-dev/rawdata/morrisons_shopping2.csv")

df


# In[ ]:




