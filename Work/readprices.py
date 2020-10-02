#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 14:54:32 2020

@author: abhijith
"""
prices = {}
with open('Data/prices.csv','rt') as f:
    for line in f:
        row = line.strip().split(',')
        if len(row)>1:
            print(row)
            prices[row[0]] = float(row[1])

print(prices)