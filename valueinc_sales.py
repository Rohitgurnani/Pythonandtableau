# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 01:26:28 2022

@author: rohit
"""

import pandas as pd

# file_name = pd.read_csv('file.csv') <------format of read_csv

data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv', sep=';')

#summary of the data
data.info()

 # working with calculations
 
 # Defining variables
 
CostPerItem = 11.76
SellingPricePerItem = 21.11
NumberofItemPurchased = 6
 
 # Mathematical Operations on Tableau
ProfitPerItem = 21.11 - 11.76
ProfitPerItem = SellingPricePerItem - CostPerItem
 
ProfitPerTransaction = ProfitPerItem*NumberofItemPurchased
CostPerTrasaction = CostPerItem*NumberofItemPurchased
SellingPricePerTransaction = SellingPricePerItem*NumberofItemPurchased

# CostPerTrasaction column Calculation 

# CostPerTransaction = CostPerItem * NumberofItemPurchased
# Variable = dataframe['column name']

CostPerItem = data['CostPerItem']
NumberofItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberofItemsPurchased

# adding a new column to a dataframe

data['CostPerTransaction'] = CostPerTransaction

# Sales Per Transaction

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

# Profit Calculation = Sales - Cost

data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

# Markup = (Sales-Cost)/Cost

data['Markup'] = ( data['SalesPerTransaction'] - data['CostPerTransaction'] )/ data['CostPerTransaction']

data['Markup'] = ( data['ProfitPerTransaction'])/ data['CostPerTransaction']

#rounding marking

roundmarkup = round( data['Markup'], 2)

data['Markup'] = round( data['Markup'], 2)

# Combining Data Fields
# my_date = data['Day']+'-'


#Checking Column Data Type
print(data['Day'].dtype)

#Change column type
Day = data['Day'].astype(str)
Year = data['Year'].astype(str)
print(Year.dtype)

my_date = Day + '-' + data['Month'] + '-' + Year

data['Date'] = my_date

#using iloc to view specific row/column

data.iloc[0] #view the row with index = 0 
data.iloc[0:3] #first 3 rows
data.iloc[-5:] #last 5 rows

data.head(5) # brings in first 5 rows
data.iloc[:,2] #bring in all the rows on the 2nd column
data.iloc[4,2] #brings in the 4th row, 2nd column

# using split to split the client_keyword field
# new_var = column.str.split('sep' , expand = True)
 
split_col = data['ClientKeywords'].str.split(',' , expand = True)

# creating new columns for the splits columns in client keywords 

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthofContract'] = split_col[2]

#using the replace function 

data['ClientAge'] = data['ClientAge'].str.replace('[' , '')
data['LengthofContract'] = data['LengthofContract'].str.replace(']' , '')

#using the lower function to change item to lowercase

data['ItemDescription'] = data['ItemDescription'].str.lower()

# bringing in a new dataset

seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

# merging files: merge_df = pd.merge(df_old, df_new, on = 'key')

data = pd.merge(data, seasons, on = 'Month')

# droping columns
#df = df.drop('columnname' , axis = 1)

data = data.drop(['ClientKeywords', 'Day', 'Month', 'Year'], axis = 1)
      
# export into csv 

data.to_csv('ValueInc_Cleaned.csv', index = False)









