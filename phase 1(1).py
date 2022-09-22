#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[ ]:





# In[3]:


# import the csv file with only useful columns
# source:  https://www.data.gouv.fr/fr/datasets/temperature-quotidienne-departementale-depuis-janvier-2018/
df = pd.read_csv("C:\\Users\\click\\Desktop\\ProductionAndCurtailmentsData_2018.csv")
df.head()


# In[6]:


df.info()


# In[3]:


Total = df['Hour'].sum()
print (Total)


# In[21]:


df = pd.read_csv("C:\\Users\\click\\Desktop\\ProductionAndCurtailmentsData_2018.csv", usecols=[0,1,2,4,5])
df.head()


# In[7]:


# Select April 2018 records only
df = df[(df["Date"]>="4/1/2018  12:00:00 AM") & (df["Date"]<="4/30/2018  11:55:00 PM")]
df.head()


# In[8]:


# Select April 2018 records only
df = df[(df["Date"]>="4/17/2018  12:00:00 AM") & (df["Date"]<"4/18/2018  12:00:00 AM")]
df.head()


# In[9]:


df.drop('Date', inplace=True, axis=1)


# In[10]:


df.head()


# In[11]:


df.plot(x = 'Hour', y = 'Wind')

plt.show()


# In[12]:


df.plot(x = 'Hour', y = 'Solar')

plt.show()


# In[13]:


column_names = ['Wind', 'Solar']
df['Total']= df[column_names].sum(axis=1)
df.head()


# In[14]:


df.plot(x = 'Hour', y = 'Total')

plt.show()


# In[63]:


df2 = df.groupby(['Hour'])['Wind'].sum()
df2.head()


# In[ ]:




