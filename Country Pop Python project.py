#!/usr/bin/env python
# coding: utf-8

# In[35]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


# In[36]:


#importing data for analysis - Using Population Growth Predictions found on Kaggle.com
POP_DF = pd.read_csv("C:/Users/austi/OneDrive/Documents/NEWapprenticeship/DATAPACKS/Country Population Growth Predictions - results-20220831-153501.csv")


# In[37]:


#Investigating the structure of the dataset
POP_DF.head(30)


# In[38]:


#Using .shape to see how many rows are in the dataset
POP_DF.shape


# In[39]:


#Determining whether or not there are any null values within
print(POP_DF.isnull())


# In[40]:


#Double checking for null values
POP_DF.isnull().sum()


# In[ ]:


#READY TO BEGIN ANALYSIS WITH A VERIFIED CLEAN DATAFILE


# In[41]:


# variable for question one
Pop_Size_DESC = POP_DF.sort_values(by = 'Population', ascending = False)


# In[67]:


# variable for question two
Low_Pop_Dens= POP_DF.sort_values(by = 'Density_Ten_Year', ascending = True)


# In[42]:


#sorting data by descending to see countries with the highest population size
Pop_Size_DESC.head(30)


# In[56]:


#Creating new variable and slicing the top ten rows
Top_ten_Countries = Pop_Size_DESC[0:10]


# In[70]:


#Plotting the top ten countries on a bar graph to give a better visual
Top_ten_Countries.plot(x = "Country", y=["Population"], kind="bar", color ="r")
plt.title('Top Ten Countries With The Highest Populations')
plt.xlabel('Countries')
plt.ylabel('Billion')


# In[68]:


##QUESTION TWO
#Using variable that was created earlier to see the countries with the lowest population densities 
Low_Pop_Dens.head(10)


# In[71]:


#Creating new variable that will hold the first ten rows of data only
Lowest_Country_Ten_Year_Dens = Low_Pop_Dens[0:10]


# In[194]:


#Isolating the number one country with the lowest population density
QTWO_df = pd.DataFrame(Lowest_Country_Ten_Year_Dens)
display(QTWO_df.iloc[0])
Mongolia = QTWO_df.iloc[0]


# In[195]:


Mongolia.info


# In[196]:


#Creating new Data frame with only necessary information
Mongolia_df = pd.DataFrame.from_dict({
    'Country': ['Mongolia'],
    'Population': [3278290],
    'Pop_Density': [2],
    'Ten_Year_Prediction' : [3819208],
    'Density_Ten_Year': [2],
    'One_Hundred_Year_Prediction': [8687469],
    'Density_One_Hundred_Year': [6]
    
})
Columns=[ 'Country','Population','Pop_Density','Ten_Year_Prediction','Density_Ten_Year',
         'One_Hundred_Year_Prediction','Density_One_Hundred_Year']


# In[197]:


#Checking for success
print(Mongolia_df)


# In[180]:


Current_Pop = 3278290
Ten_Year_Pop = 3819208 
One_Hundred_Year_Pop = 8687469
print(Ten_Year_Pop - Current_Pop)


# In[181]:


Growth_Per_Year = (540918 // 10)


# In[182]:


print(Growth_Per_Year)


# In[183]:


print(Growth_Per_Year/One_Hundred_Year_Pop)


# In[193]:


Mongolia_df.plot.bar()


# In[ ]:




