#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd


# In[5]:


data=pd.read_csv("C:/Users/Vivek/OneDrive/Documents/covid 2020.csv")
data


# In[7]:


data.head()


# In[8]:


#Q1: Show the no. of confirmed cases, Deaths & Recovered Cases in each region?


# In[15]:


data.groupby(["Region"],as_index=False).sum()


# In[ ]:


#Q2:- Remove all the records where Confirmed Cases is Less than 10.


# In[20]:


data[~(data.Confirmed<10)]
data


# In[21]:


#In which region, maximum number of confirmed cases were recorded?


# In[39]:


max_cases=data.groupby(["Region"],as_index=False)["Confirmed"].sum().sort_values(by="Confirmed",ascending=False)
max_cases.head(1)


# In[40]:


#Q4:- In which region, maximum number of Deaths cases were recorded?


# In[44]:


max_death=data.groupby(["Region"],as_index=False)["Deaths"].sum().sort_values(by="Deaths",ascending=False)
max_death.head(1)


# In[45]:


#Q5:- How many Confirmed, Deaths and Recovered cases were reported from India till 29th April 2020?


# In[47]:


data[data["Region"]=="India"]


# In[48]:


#Q6:- (A) Sort the enitre data with respect to No. of Confirmed Cases in ascending order.

#(B) Sort the enitre data with respect to No. of Recovered Cases in descending order.


# In[50]:


data.sort_values(by="Confirmed")


# In[51]:


data.sort_values(by="Recovered",ascending=False)

