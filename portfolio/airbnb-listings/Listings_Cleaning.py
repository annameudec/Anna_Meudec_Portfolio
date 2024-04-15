#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing Libraries
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Handling the Dataset. 

Inpath= "C:/Users/kelli/Documents/DCU/Y4/Mt-412 Analytics Portfolio/"
Airbnb_Df=pd.read_excel(Inpath+"Listings Power BI Assignmnet.xlsx"
                   ,header=0, index_col=0)
Airbnb_Df


# In[2]:


#Describe the dataset 
print(Airbnb_Df.head())
print(Airbnb_Df.tail())
print(Airbnb_Df.shape)


# In[3]:


Airbnb_Df.describe(include="all")


# In[4]:


#Handling missing / Nan values
(Airbnb_Df.isna().sum(axis=0)) 
print(Airbnb_Df.isna().sum(axis=0)/len(Airbnb_Df))


# In[5]:


#As we will not be using the values within district and the null values were so high we dropped the column. 
Airbnb_Df.drop("district", axis=1,inplace=True)
Airbnb_Df


# In[6]:


Airbnb_Df.describe(include="all")


# In[7]:


#Checking that the column has been dropped from the dataframe. 
list(Airbnb_Df.columns)


# In[8]:


# After checking that the null values were evenly distributed by country we decided to drop the rows with null values for the reviews. 
Airbnb_Df.dropna(subset=["review_scores_rating","review_scores_accuracy","review_scores_cleanliness","review_scores_checkin", 
                         "review_scores_communication", "review_scores_location", "review_scores_value"], inplace=True)
Airbnb_Df


# In[9]:


#Handling missing / Nan values
(Airbnb_Df.isna().sum(axis=0)) 
print(Airbnb_Df.isna().sum(axis=0)/len(Airbnb_Df))


# In[10]:


# We chose to keep the columns host_response_time, host_response_rate, host_acceptance_rate as we would loose too much valuable data. 
# We will use filters to drop null values within power bi when specifically looking at these measures. 


# In[ ]:


Airbnb_Df.describe(include="all")


# In[ ]:


#Checking for duplicated rows, deleting them while keeping the first instance. 
#print("There are " + str(Airbnb_Df.duplicated().sum()) + " duplicated Rows")

Airbnb_Df[Airbnb_Df.index.duplicated()]


# In[11]:


Airbnb_Df.to_excel(Inpath + 'Listings Power BI Assignmnet_Cleaned.xlsx', index=True)


# In[12]:





# In[19]:




