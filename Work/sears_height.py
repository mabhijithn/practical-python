# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

ht_bill = 0.11*0.001
ht_sears = 445
num_bills = 1
num_days = 1

while (num_bills*ht_bill)<ht_sears:
    num_bills = num_bills*2
    num_days = num_days+1

print('Number of days required = ', num_days,'Number of bills = ', num_bills)