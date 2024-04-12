#!/usr/bin/env python
# coding: utf-8

# In[32]:


#Importing Libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[33]:


#Handling the Dataset

BnB_Df = pd.read_csv(r"C:\Users\annam\Documents\Assignments\US_BNB_2023.csv", low_memory=False)

BnB_Df.describe()


# In[34]:


#Describing the dataset

#Printing the first 5 rows of the DataFrame
print(BnB_Df.head())

#Printing the last 5 rows of the DataFrame
print(BnB_Df.tail())

#Printing the shape of the DataFrame (number of rows and columns)
print(BnB_Df.shape)


# In[30]:


#Generating descriptive statistics for all columns in the DataFrame, including categorical variables
BnB_Df.describe(include="all")


# In[9]:


#Handling missing / Nan values
(BnB_Df.isna().sum(axis=0)) 
print(BnB_Df.isna().sum(axis=0)/len(BnB_Df))


# In[10]:


#Filling missing values in the "neighbourhood_group" column with "Not Specified"
BnB_Df["neighbourhood_group"].fillna(value="Not Specified", inplace=True)

#Calculating the proportion of missing values in each column of the DataFrame
#by dividing the sum of missing values by the total length of the DataFrame
(BnB_Df.isna().sum(axis=0)/len(BnB_Df))


# In[36]:


#Dropping rows where any of the specified columns have missing values
#These columns include "reviews_per_month", "last_review", "name", and "host_name"
BnB_Df.dropna(subset=["reviews_per_month","last_review","name","host_name"], inplace=True)
BnB_Df

#Displaying the DataFrame after dropping the specified rows
print(BnB_Df)


# In[12]:


#Checking for duplicated rows, deleting them while keeping the first instance. 
print("There are " + str(BnB_Df.duplicated().sum()) + " duplicated Rows")

#Return duplicated rows
duplicated_rows = BnB_Df[BnB_Df.duplicated(keep=False)]
print(duplicated_rows)

#Remove duplicated rows. 
BnB_Df_unique=BnB_Df.drop_duplicates(keep="first")
BnB_Df_unique


# In[13]:


#Investigating categorical data. 
BnB_Df_unique.describe(include="object")


# In[14]:


#Investigating Numerical data. 
BnB_Df_unique.describe(include=np.number)


# In[15]:


#Looking at the difference between the Mean, 75th percentile and the Max values of the "minimum_nights" variable.
#We identified that we should remove values above 365 (the number of days in a year). 
BnB_Df_unique= BnB_Df_unique[BnB_Df_unique["minimum_nights"]<=365]
BnB_Df_unique.describe(include=np.number)


# In[16]:


#Investigating "reviews_per_month" feature. The max value seemed high as there are only 
#30 days in a month and there is a 14 day window for completing a review. 

#Examining through percentiles.
percentiles = [25, 50, 75, 90, 95]  

percentiles.extend([i/10 for i in range(990, 1000, 1)] + [100])

#Calculate the percentiles of the 'price' column
price_percentiles = np.percentile(BnB_Df['reviews_per_month'], percentiles)

#Print the calculated percentiles
for percentile, value in zip(percentiles, price_percentiles):
    print(f'{percentile}th Percentile: {value:.2f}')


# In[17]:


#It is clear from the percentiles that 101.42 is an outlier so we will 
#keep values less than or equal to 13.22
BnB_Df_unique= BnB_Df_unique[BnB_Df_unique["reviews_per_month"]<=13.23]
BnB_Df_unique.describe(include=np.number)


# In[37]:


#Creating a new DataFrame containing only the numeric columns from BnB_Df_unique
BnB_Df_unique_numeric=BnB_Df_unique[["latitude","longitude","price","minimum_nights"
                                     ,"number_of_reviews","reviews_per_month"
                                     ,"availability_365","number_of_reviews_ltm"]]

#Displaying the new DataFrame
BnB_Df_unique_numeric


# In[39]:


#Choosing z-score or IQR method for smoothing out large data.

#Calculating the mean and standard deviation of the "price" column in BnB_Df_unique_numeric
mean_BnB_Df_unique_numeric=BnB_Df_unique_numeric["price"].mean()
std_BnB_Df_unique_numeric=BnB_Df_unique_numeric["price"].std()

#Calculating the upper and lower bounds for outliers using the Z-score method
Upper_bound=mean_BnB_Df_unique_numeric+3*std_BnB_Df_unique_numeric
Lower_bound=mean_BnB_Df_unique_numeric-3*std_BnB_Df_unique_numeric

#Printing the upper and lower bounds for outliers
print("Upper Bound")
print(Upper_bound)
print("Lower Bound")
print(Lower_bound)

#Filtering the DataFrame to include only rows with prices within the upper and lower bounds
Z_Out_BnB_Df_unique_numeric=BnB_Df_unique_numeric[(BnB_Df_unique_numeric["price"]>Lower_bound) 
                                   & (BnB_Df_unique_numeric["price"]<Upper_bound)]

#Displaying the filtered DataFrame without Z-score outliers
Z_Out_BnB_Df_unique_numeric


# In[40]:


#Identify the upper and lower bounds using the IQR method for the ‘price’ variable

#Calculating the first and third quartiles (Q1 and Q3) of the "price" column in BnB_Df_unique_numeric
Q1=BnB_Df_unique_numeric["price"].quantile(.25)
Q3=BnB_Df_unique_numeric["price"].quantile(.75)

#Printing the values of Q1 and Q3
print("Q1=", Q1)
print("Q3= ", Q3)

#Calculating the interquartile range (IQR)
IQR=Q3-Q1
print("IQR= ", IQR)

#Calculating the lower and upper bounds for outliers using the IQR method
Lwr_bound=Q1-1.5*IQR
Upr_bound=Q3+1.5*IQR
print("Lower Bound= ",Lwr_bound)
print("Upper Bound= ",Upr_bound)

#Filtering the DataFrame to include only rows with prices within the lower and upper bounds
IQR_Out_BnB_Df_unique_numeric=BnB_Df_unique_numeric[(BnB_Df_unique_numeric["price"]>Lwr_bound) &
                                                    (BnB_Df_unique_numeric["price"]<Upr_bound)]

#Displaying the filtered DataFrame without IQR outliers
IQR_Out_BnB_Df_unique_numeric


# In[41]:


#Investigating into which method would remove more data for further understanding of the data.

#Calculating the number of points removed using the Z-score method
print('Number of point removed with the z-score method: ' + str(len(BnB_Df_unique_numeric) - len(Z_Out_BnB_Df_unique_numeric)))

#Calculating the number of points removed using the IQR method
print('Number of point removed with the IQR method: ' + str(len(BnB_Df_unique_numeric) - len(IQR_Out_BnB_Df_unique_numeric)))


# In[42]:


#Investigate if the dataset is Normally distributed in order to choose a method. 

#Calculate skewness for all columns
skewness = BnB_Df_unique_numeric.skew()

#Printing the skewness values
print("Skewness:")
print(skewness)

#Calculate kurtosis for all columns
kurtosis = BnB_Df_unique_numeric.kurtosis()

#Printing the kurtosis values
print("\nKurtosis:")
print(kurtosis)


# In[43]:


#Printing the minimum values for each column in IQR_Out_BnB_Df_unique_numeric.
print('     Min values')
pd.set_option('display.float_format', '{:.0f}'.format)
print(IQR_Out_BnB_Df_unique_numeric.min())

#Printing the maximum values for each column in IQR_Out_BnB_Df_unique_numeric.
print('     Max values')
pd.set_option('display.float_format', '{:.0f}'.format)
print(IQR_Out_BnB_Df_unique_numeric.max())


# In[24]:


#As the majority of the data is not normally distributed and our 
#data contains extreme outliers in the price column we will use the IQR to smooth out the data. 


# In[45]:


#Smooth out the large values in noOutlrIqrDf using the logarithm (np.log) and display the min and max
IQR_Out_BnB_Df_unique_numeric_log = IQR_Out_BnB_Df_unique_numeric.apply(np.log)

#Displaying the DataFrame after applying the natural logarithm transformation
IQR_Out_BnB_Df_unique_numeric_log


# In[46]:


#Printing the minimum values for each column in IQR_Out_BnB_Df_unique_numeric_log
print('     Min values')
print(IQR_Out_BnB_Df_unique_numeric_log.min())

#Printing the maximum values for each column in IQR_Out_BnB_Df_unique_numeric_log
print('     Max values')
print(IQR_Out_BnB_Df_unique_numeric_log.max())

#Negative infinity returned due to zero values. 
#Nan returned due to negative values. 
#After consideration all of the values we are content to accept the log function. 


# In[48]:


#Displaying the distribution of the "price" after smoothing using the log transformation.

#Setting up the figure size
plt.figure(figsize=(12, 5))

#Creating subplots for before and after log transformation histograms
plt.subplot(1, 2, 1)

#Plotting histogram for the 'price' column before log transformation
sns.histplot(IQR_Out_BnB_Df_unique_numeric['price'], color="r", bins=30)
plt.title('Distribution of Price (Before Log Transformation)')
plt.xlabel("Price")

plt.subplot(1, 2, 2)

#Plotting histogram for the 'price' column after log transformation
sns.histplot(IQR_Out_BnB_Df_unique_numeric_log['price'], color="g", bins=30)
plt.title('Distribution of Price (After Log Transformation)')
plt.xlabel("Price")

#Displaying the plot
plt.show()


# In[28]:


#Now it can be seen that all of the data is within the acceptable bounds of -7 and 7. 
IQR_Out_BnB_Df_unique_numeric.describe()


# In[49]:


#Assigning the DataFrame to a variable for clarity
numerical_data=IQR_Out_BnB_Df_unique_numeric

#Merging numerical_data with selected columns from BnB_Df_unique
merged_BnB_Df = pd.merge(numerical_data, BnB_Df_unique[["neighbourhood","room_type","city"]], left_index=True, right_index=True)

#Displaying the merged dataset
print(merged_BnB_Df)
merged_BnB_Df

