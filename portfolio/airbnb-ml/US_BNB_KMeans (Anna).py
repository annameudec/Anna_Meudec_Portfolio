#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing Libraries
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler 

#Handling the Dataset.

#Reading the cleaned dataset from CSV file
merged_BnB_Df = pd.read_csv(r"C:\Users\annam\Documents\US_BNB_2023_Cleaned.csv", low_memory=False)

#Generating descriptive statistics for the dataset
merged_BnB_Df.describe()


# In[2]:


#Creating two new columns in BnB_Df_unique called "avg_price_neigh" and "avg_price_city" which will contain 
#the average price per neighbourbood and city. 

#Calculating the average price per neighborhood
avg_price_neigh = merged_BnB_Df.groupby('neighbourhood')['price'].transform('mean')

#Creating a new column 'avg_price_neigh' which contains the price divided by the average price of its neighborhood
merged_BnB_Df['avg_price_neigh'] = merged_BnB_Df['price'] / avg_price_neigh

#Displaying the 'avg_price_neigh' column
merged_BnB_Df['avg_price_neigh']

#Creating a new column in BnB_Df_unique called "avg_price_city" which will contain the average price per city.

#Calculating the average price per city
avg_price_neigh = merged_BnB_Df.groupby('city')['price'].transform('mean')

#Creating a new column 'avg_price_city' which contains the price divided by the average price of its city
merged_BnB_Df['avg_price_city'] = merged_BnB_Df['price'] / avg_price_neigh

#Displaying the 'avg_price_city' column
merged_BnB_Df['avg_price_city']

#Assuming that properties with more reviews have higher satisfaction rates as if the reviews 
#were negative they would not get as many bookings and therefore not have a high number of reviews. 
#create a feature called "customer_satisfaction"

#Creating a new column 'customer_satisfaction' which represents the ratio of number of reviews to availability_365
merged_BnB_Df["customer_satisfaction"]=merged_BnB_Df["number_of_reviews"]/merged_BnB_Df["availability_365"]

#Displaying the DataFrame with the new column added
merged_BnB_Df


# In[6]:


#############################################################
#                     K-Means                               #
#############################################################

#Removing all catagorical columns to allow for ploting
merged_BnB_Df_cluster=merged_BnB_Df.drop(["neighbourhood","city","room_type","customer_satisfaction"],axis=1)

#Displaying the DataFrame after removing categorical columns to prepare for clustering.
merged_BnB_Df_cluster


# In[ ]:


#Testing to ensure that we could plot the information without errors before commencing K-Means
plt.plot(merged_BnB_Df_cluster)

#Displaying the graph
plt.show()


# In[ ]:


#Finding the Optimal number of "K" Clusters

#Initialising a list called "inertia"
#This list will store the inertia.
#Observing the behaviour of the inertia as the no. of clusters increases.
inertia = []

#Using a for loop, testing all the values of k from 1 to 12 (included) with a step of 1.
#At each iteration run the k-means algorithm using k no. of clusters.
#It then stores the values of k and of the inertia at each iteration in the "inertia" list.
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(merged_BnB_Df_cluster)
    inertia.append(kmeans.inertia_)

#Plotting
plt.plot(range(1, 11), inertia, marker='o')
plt.title('Elbow Method for Optimal k')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Distance')
plt.show()


# In[ ]:


#Based on the elbow method and plotting our graph, we deemed our optimal value for k to be 2.
#Note: The graph is quite curved and an argument could be made for either 2 or 4. However, we opted for 2.

#Setting the optimal number of clusters (k) determined from the Elbow Method
optimal_k = 2

#Initialising the KMeans clustering algorithm with the optimal number of clusters
kmeans = KMeans(n_clusters=optimal_k, random_state=42)

#Fitting the KMeans model to the data and assigning cluster labels to each data point
merged_BnB_Df['Cluster'] = kmeans.fit_predict(merged_BnB_Df_cluster)

#Creating a new column called "Cluster", to store the labels given by the k-means.
print(merged_BnB_Df['Cluster'].value_counts())

#Displaying the DataFrame with the newly added "Cluster" column.
merged_BnB_Df


# In[ ]:




