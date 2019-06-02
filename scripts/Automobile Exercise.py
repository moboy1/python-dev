#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
df = pd.read_csv("C:/Users/mgaye_ext/Work/training/python-dev/rawdata/Automobile_data.csv")

#List first 5 records 
df.head()


# In[17]:


#List last 5 records
df.tail()


# In[18]:


#Replace all column values which contain ‘?’ and n.a with NaN after csv read
df.replace({'?':np.nan, 'n.a':np.nan})
print (df)
df.to_csv("C:/Users/mgaye_ext/Work/training/python-dev/rawdata/Automobile_data.csv")


# In[39]:


#Find the most expensive car company name 
df[['company','price']][df.price==df['price'].max()]


# In[16]:


#Find the Fastest and least expensive car company name 
df[['company','horsepower','price']][(df.horsepower>200) & (df.price<35000)]


# In[22]:


#Print All mercedes-benz Cars details
car_make=df.groupby('company')
mercedesDf=car_make.get_group('mercedes-benz')
mercedesDf


# In[19]:


#Count total cars per company
df['company'].value_counts()


# In[23]:


#Find each company’s Higesht price car and sort by price
car_make=df.groupby('company')
most_expensive_car_by_company=car_make['company','price'].max().sort_values(by=['price'], ascending=False)
most_expensive_car_by_company


# In[81]:


#Find the average mileage of each car making company and sorted
car_make=df.groupby('company')
average_mile_of_company=car_make['company','average-mileage'].mean().sort_values(by=['average-mileage'], ascending=False)
average_mile_of_company


# In[79]:


#Find the fastest car for each company and sorted
car_make=df.groupby('company')
fastest_car_for_company=car_make['company','horsepower'].max().sort_values(by=['horsepower'], ascending=False)
fastest_car_for_company


# In[77]:


#Concatenate two data frames using following conditions
car_make=df.groupby('company')
fastest_car_for_company=car_make['company','horsepower'].max().sort_values(by=['horsepower'], ascending=False)

american_cars=fastest_car_for_company[fastest_car_for_company['company'].isin(['dodge','chevrolet'])]
german_cars=fastest_car_for_company[fastest_car_for_company['company'].isin(['volkswagen','audi','bmw','mercedes-benz','porsche'])]
amergerman_cars=pd.concat([american_cars, german_cars], keys=["America", "Germany"])

amergerman_cars


# In[78]:


#Merge two data frames using following conditions
car_make=df.groupby('company')
fastest_car_for_company=car_make['company','horsepower','price'].max().sort_values(by=['horsepower'], ascending=False)

american_cars=fastest_car_for_company[fastest_car_for_company['company'].isin(['dodge','chevrolet'])]
german_cars=fastest_car_for_company[fastest_car_for_company['company'].isin(['volkswagen','audi','bmw','mercedes-benz','porsche'])]
amergerman_cars=pd.merge(american_cars, german_cars, on="company")

amergerman_cars


# In[ ]:




