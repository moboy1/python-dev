#!/usr/bin/env python
# coding: utf-8

# In[110]:


import pandas as pd
from bs4 import BeautifulSoup
import requests
url="https://www.rightmove.co.uk/house-prices/detail.html?locationIdentifier=POSTCODE%5E1040636&searchLocation=CR0+6HU&radius=15.0"
r  = requests.get(url)
data = r.text
html=BeautifulSoup(data)
total_listings=html.find_all("div", {"class": "soldDetails"})

df=pd.DataFrame(columns=('property_address', 'property_price', 'property_type', 'property_date_sold', 'property_no_of_beds'))
i=0
for listings in total_listings:
    if listings.a != None:
        paddress=listings.a.text
    elif listings.div != None:
        paddress=listings.div.text
    
    for listing in listings.find_all('tr'):
        for listing_price in listing.find_all('td', {'class': 'soldPrice'}):
            if listing_price.text != None:
                pprice=listing_price.text.replace('£','').replace(',','')
        for listing_type in listing.find_all('td', {'class': 'soldType'}):
            if listing_type.text != None:
                ptype=listing_type.text
        for listing_date in listing.find_all('td', {'class': 'soldDate'}):
            if listing_date.text != None:
                pdate=listing_date.text
        for listing_beds in listing.find_all('td', {'class': 'noBed'}):
            if listing_beds.text != None:
                pbeds=listing_beds.text
            
        df.loc[i] = [paddress, pprice, ptype, pdate, pbeds]
        i+=1

df.property_price = df.property_price.astype(int)
#df['property_price'] = df['property_price'].map('£{:,.2f}'.format)
df


# In[109]:


property_address=df.groupby('property_address')
most_expensive_property_per_address=property_address['property_address','property_price'].max().sort_values(by=['property_price'], ascending=False)
most_expensive_property_per_address


# In[66]:


properties_per_address=df['property_address'].value_counts()
properties_per_address


# In[71]:


property_address=df.groupby(['property_address','property_no_of_beds']).size()
property_address


# In[108]:


property_address=df.groupby('property_address')
avg_price_of_property_per_address=property_address['property_address','property_price'].mean().sort_values(by=['property_price'], ascending=False)
avg_price_of_property_per_address


# In[ ]:




