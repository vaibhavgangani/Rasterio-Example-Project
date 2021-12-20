#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing rasterio python module
import rasterio as rio


# In[3]:


# read image
image_data = rio.open(r"udaipurdem.tif")


# In[7]:


#assigning coordinates, can be done in an array
row, col = image_data.index(73.3195,24.3228)# -*- coding: utf-8 -*-


# In[8]:


#reading data or array
arr=image_data.read()


# In[9]:


#creating a new variable
value=arr[0][row,col]


# In[10]:


#final output
print(value)

