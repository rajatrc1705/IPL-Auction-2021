# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 18:45:39 2021

@author: rajat
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# We write a function to import our data from the csv file

df = pd.read_csv('auction.csv')

# Role column of dataframe has some odd data, we need to clean that...

df['Role'].unique()

for ind in df.index:
    if df['Role'][ind] == 'Indi':
        print(ind, df['Name'][ind])
        
# Mujtaba is an All-Rounder but we don't know which one, so we replace him with the type of all-rounders with most abundance
df['Role'] = df['Role'].replace(['Indi'], 'Bowling Allrounder')

# We need to clean the data related to prices also, converting all the prices into 'Lakhs'. We will also have some rows with 
# no "sold price" as those players have gone unsold. We write 2 functions to do the same.

def base_price(df):
    base_p = list()
    for ind in df['Base_Price'].index:
        string = df['Base_Price'][ind].split('  ')
        if string[1] == 'Crore':
            base_p.append(float(string[0])*100)
        else:
            base_p.append(float(string[0]))
    return base_p

def final_price(df):

    final_price = list()

    for ind in df['Final_Price'].index:
        # print(df['Final_Price'][ind].split('  '))
        if df['Final_Price'][ind] != '-':
            string = df['Final_Price'][ind].split('  ')
            price = float(string[0])
            # print(price)
            if string[1] == 'Crore':
                price = price * 100
                final_price.append(price)
            else:
                final_price.append(price)
        else:
            final_price.append(df['Final_Price'][ind])
    return final_price


def price_function(df):

    base = np.array((df['Base_Price']))
    
    # replacing unsold player's final value with 0
    final = np.array((df['Final_Price']))
    final[final == '-'] = 0
    
    return base, final

df['Base_Price'] = base_price(df)
df['Final_Price'] = final_price(df)
df['Base_Price'], df['Final_Price'] = price_function(df)

df.to_csv('cleaned_data.csv')