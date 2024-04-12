#!/usr/bin/env python
# coding: utf-8

# In[14]:


#Importing Libraries
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

#Handling the Dataset.

#Reading the cleaned dataset from CSV file
merged_BnB_Df = pd.read_csv(r"C:\Users\annam\Documents\Assignments\US_BNB_2023_Cleaned.csv", low_memory=False)

#Generating descriptive statistics for the dataset
merged_BnB_Df.describe()


# In[7]:


#############################################################
#                     Feature Engineering                   #
#############################################################

#Creating two new columns in BnB_Df_unique called "avg_price_neigh" and "avg_price_city" which will contain 
#the average price per neighbourbood and city. 

#Calculating the average price per neighborhood
avg_price_neigh = merged_BnB_Df.groupby('neighbourhood')['price'].transform('mean')

#Creating a new column 'avg_price_neigh' which contains the price divided by the average price of its neighborhood
merged_BnB_Df['avg_price_neigh'] = merged_BnB_Df['price'] / avg_price_neigh

#Displaying the 'avg_price_neigh' column
merged_BnB_Df['avg_price_neigh']


# In[10]:


#Creating a new column in BnB_Df_unique called "avg_price_city" which will contain the average price per city.

#Calculating the average price per city
avg_price_neigh = merged_BnB_Df.groupby('city')['price'].transform('mean')

#Creating a new column 'avg_price_city' which contains the price divided by the average price of its city
merged_BnB_Df['avg_price_city'] = merged_BnB_Df['price'] / avg_price_neigh

#Displaying the 'avg_price_city' column
merged_BnB_Df['avg_price_city']


# In[11]:


#Creating dummy variables for the 'room_type' column and adding them to the DataFrame
#Using One-Hot Encoding on the nominal variable "room_type". 
merged_BnB_Df = pd.get_dummies(merged_BnB_Df, columns=['room_type'], prefix='property_type')

#Displaying the DataFrame with the added dummy variables
merged_BnB_Df


# In[12]:


#Assuming that properties with more reviews have higher satisfaction rates as if the reviews 
#were negative they would not get as many bookings and therefore not have a high number of reviews. 
#create a feature called "customer_satisfaction"

#Creating a new column 'customer_satisfaction' which represents the ratio of number of reviews to availability_365
merged_BnB_Df["customer_satisfaction"]=merged_BnB_Df["number_of_reviews"]/merged_BnB_Df["availability_365"]

#Displaying the DataFrame with the new column added
merged_BnB_Df


# In[ ]:




