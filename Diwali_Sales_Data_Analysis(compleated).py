#!/usr/bin/env python
# coding: utf-8

# Data Cleaning 

# In[6]:


#importing python libraries 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[67]:


df = pd.read_csv(r"C:\Users\SOUMYODEEP\Downloads\Diwali Sales Data\Diwali Sales Data.csv", encoding= "unicode_escape") 
# used the unicode function to avoid unwanted errors  


# In[18]:


df.shape


# In[21]:


df.head(10)


# In[22]:


df.info()


# In[23]:


df.drop(["Status", "unnamed1"], axis = 1, inplace = True)


# In[29]:


pd.isnull(df)


# In[30]:


pd.isnull(df).sum()


# In[36]:


#Drop Null Values/removing errors/Data cleaning
df.dropna(inplace= True)


# In[37]:


#Changing Data type from float to integer

df["Amount"] = df["Amount"].astype('int')


# In[53]:


df["Amount"].dtypes


# Exploratory Data Analysis

# In[40]:


df.columns


# In[12]:


ax = sns.countplot(x = 'Gender', data = df)
for bars in ax.containers:
    ax.bar_label(bars)


# In[11]:


sales_gender = df.groupby(["Gender"], as_index = False)["Amount"].sum().sort_values(["Amount"], ascending = False)

sns.barplot(x = 'Gender', y = 'Amount', data = sales_gender)


# From the graph, it can be cited that most of the buyers are female and they also have a greater purchasing power

# Analysis by Age 

# In[10]:


ax = sns.countplot(data = df, x= "Age Group", hue = "Gender")
for bars in ax.containers:
    ax.bar_label(bars)


# In[21]:


sales_age_grp = df.groupby(["Age Group"], as_index = False)["Amount"].sum().sort_values(["Amount"], ascending = False)

sns.barplot(x = "Age Group", data = sales_age_grp, y = 'Amount') 


# **Most of the buyers are femlaes having age between 26-35

# Analysis By State 

# In[22]:


df.columns


# In[68]:


#States which has a higher frequency of orders/ high no of orders
sales_state = df.groupby(["State"], as_index = False)["Orders"].sum().sort_values(["Orders"], ascending = True).head(10)
sns.set(rc={'figure.figsize':(15, 5)})
sns.barplot(x = 'State', data = sales_state, y = 'Orders')


# In[37]:


#Staes which has a higher amount of orders
sales_state = df.groupby(["State"], as_index = False)["Amount"].sum().sort_values(["Amount"], ascending = False).head(10)
sns.set(rc={'figure.figsize':(15, 5)})
sns.barplot(x = 'State', data = sales_state, y = 'Amount')


# In[47]:


df.columns


# In[57]:


#which industry contributed more for our annual sales 
sales_Occ = df.groupby(["Occupation"], as_index = False)["Amount"].sum().sort_values(["Amount"], ascending = False).head(5)

sns.barplot(x = 'Occupation', data = sales_Occ, y = 'Amount')


# It is clear that most of the female consumers resulting in higher sales are working in following industries. 

# In[59]:


#Which Product lines has higher amount of sales
sales_Items = df.groupby(["Product_Category"], as_index = False)["Amount"].sum().sort_values(["Amount"], ascending = False).head(5)
sns.set(rc={'figure.figsize':(10, 3)})
sns.barplot(x = 'Product_Category', data = sales_Items, y = 'Amount')


# In[56]:


# Which product lines has highest no of orders
sales_Pc = df.groupby(["Product_Category"], as_index = False)["Orders"].sum().sort_values(["Orders"], ascending = False).head(5)

sns.barplot(x = 'Product_Category', data = sales_Pc, y = 'Orders')


# Marital status of consumers 

# In[61]:


df.columns


# In[65]:


sales_MS = df.groupby(["Marital_Status", "Gender"], as_index = False)["Amount"].sum().sort_values(["Amount"], ascending = False).head(5)
sns.set(rc={'figure.figsize':(7, 5)})
sns.barplot(x = 'Marital_Status', data = sales_MS, y = 'Amount', hue = "Gender")


# Conclusion :
# It's clear from the analysis that the married Women from UP, Maharastra and Karnataka with age of 26-35, working in IT, Health Care and Aviation industry likely to buy the food, clothing & apparel and electronics gadegts and resulted for most of the overall sales, revenue and profit.

# In[ ]:




