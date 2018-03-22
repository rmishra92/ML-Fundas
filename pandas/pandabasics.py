# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 23:00:34 2018

@author: IC020549
"""
import pandas as pd

data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
        'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions', 'Lions', 'Lions'],
        'wins': [11, 8, 10, 15, 11, 6, 10, 4],
        'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
football = pd.DataFrame(data, columns=['year', 'team', 'wins', 'losses'])
print(football)

# Reading from CSV
#---------------------
from_csv = pd.read_csv('temp.csv')
from_csv.head()

# Name the column headers if we don't have
#------------------------------------------
cols = ['num', 'game', 'date', 'team', 'home_away', 'opponent',
        'result', 'quarter', 'distance', 'receiver', 'score_before',
        'score_after']
no_headers = pd.read_csv('peyton-passing-TDs-2012.csv', sep=',', header=None,
                         names=cols)
no_headers.head()

# Read from Excel
#------------------------------------------
football = pd.read_excel('football.xlsx', 'Sheet1')
football

# Fetch the text from the URL and read it into a DataFrame
#------------------------------------------
from_url = pd.read_table(url, sep='\t')
from_url.head(3)