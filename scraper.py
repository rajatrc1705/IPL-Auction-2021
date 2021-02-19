# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 23:14:35 2021

@author: rajat
"""

import pandas as pd
import numpy as np
import time
from selenium import webdriver

driver = webdriver.Chrome()
link = 'https://www.cricbuzz.com/cricket-series/ipl-2021/auction/completed'
driver.get(link)
time.sleep(5)
element = driver.find_element_by_xpath("//div[@class = 'cb-col cb-col-67 cb-scrd-lft-col']")
string = element.text

data = (string.split("\n"))
all_player = list()
player = list()
while data != []:

    if data[2] == 'SOLD':
        player = data[:9]
        data = data[9:]
        all_player.append(player)
    if data[2] == 'UNSOLD':
        player = data[:8]
        data = data[8:]
        all_player.append(player)
    player = list()
    
name = list()
speciality = list()
status = list()
base_price = list()
final_price = list()
team = list()

for player in all_player:
    name.append(player[0])
    speciality.append(player[1])
    status.append(player[2])
    base_price.append(player[4])
    final_price.append(player[6])
    if player[2] == 'SOLD':
        team.append(player[8])
    else:
        team.append(None)
        
        
role = list()
for i in speciality:
    position = i.find('•')
    role.append(i[:position].strip())
    
df = pd.DataFrame({'Name': name,
                   'Role': role,
                   'Status': status,
                   'Base_Price': base_price,
                   'Final_Price': final_price,
                   'Team': team})

df.to_csv('auction.csv')
