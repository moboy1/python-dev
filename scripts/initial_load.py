#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pandas as pd

df=pd.read_csv("C:/Users/mgaye_ext/Work/training/python-dev/rawdata/birth-registrations-by-month-since_january-2010-to-march-2012.csv")

num_rows=df.shape[0]
num_cols=df.shape[1]
headers=df.iloc[0]
first10=df.head(10)

print("Number of Rows: " + str(num_rows))
print("Number of Columns: " + str(num_cols))
print(headers)
print(first10)


# In[ ]:




