# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 12:52:51 2020

@author: Ken
"""

# import exploration files 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

file_path = 'path_to_data.csv'

# read in data 
data = pd.read_csv(file_path)


############################################################################## 
#Data Exploration
##############################################################################

#rows and columns returns (rows, columns)
data.shape

#returns the first x number of rows when head(num). Without a number it returns 5
data.head()

#returns the last x number of rows when tail(num). Without a number it returns 5
data.tail()

#returns an object with all of the column headers 
data.columns

#basic information on all columns 
data.info()

#gives basic statistics on numeric columns
data.describe()

#shows what type the data was read in as (float, int, string, bool, etc.)
data.dtypes

#shows which values are null
data.isnull()

#shows which columns have null values
data.isnull().any()

#shows for each column the percentage of null values 
data.isnull().sum() / data.shape[0]

#plot histograms for all numeric columns 
data.hist() 


############################################################################## 
#Data Manipulation
##############################################################################

# rename columns 
data.rename(index=str columns={'col_oldname':'col_newname'})

# view all rows for one column
data.col_name 
data['col_name']

# multiple columns by name
data[['col1','col2']]
data.loc[:['col1','col2']]

#columns by index 
data.iloc[:,[0:2]]

# drop columns 
data.drop('colname', axis =1) #add inplace = True to do save over current dataframe
#drop multiple 
data.drop(['col1','col2'], axis =1)

#lambda function 
data.apply(lambda x: x.colname**2, axis =1)

# pivot table 
pd.pivot_table(data, index = 'col_name', values = 'col2', columns = 'col3')

# merge  == JOIN in SQL
pd.merge(data1, data2, how = 'inner' , on = 'col1')

# write to csv 
data.to_csv('data_out.csv')
