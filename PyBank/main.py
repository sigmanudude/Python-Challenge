#!/usr/bin/env python
# coding: utf-8

# In[198]:


import csv

import os


hw_name = ("Desktop/budget_data.csv")


max_profit = 0
max_profit_month = ""
min_profit = 0
min_profit_month = ""
total_months = 0
total_profit = 0
max_change = 0
min_change = 0
total_change = 0


with open(hw_name, 'r') as csvfile:
    csv_data = csv.reader(csvfile)
    
    #gets rid of header
    next(csv_data)
    
    previous_profit = 0
    first_month = True

    for line in csv_data:
        profit = float(line[1])
        if first_month:
            first_month = False
        else:
            change = profit - previous_profit
            if max_change < change:
                max_change = change
            if min_change > change:
                min_change = change
            total_change += change
        total_profit += profit
        if max_profit < profit: #max profit
            max_profit = profit
            max_profit_month = line[0]
        if min_profit > profit: #min profit
            min_profit = profit
            min_profit_month = line[0]
        total_months += 1 #total months
        previous_profit = profit



average_change = round(total_change / (total_months - 1), 2)



print(total_months)
print(total_profit)
print(max_change)
print(min_change)
print(max_profit)
print(max_profit_month)
print(min_profit)
print(min_profit_month)

with open('testfile.txt', 'w') as f:
    print("Total Months: {}".format(total_months), file = f)
    print("Total Profit ${}".format(total_profit), file = f)
    print("Average Change: {}".format(average_change), file = f),
    print("Max profit in {} was ${}".format(max_profit_month, max_profit), file = f)
    print("Min profit in {} was ${}".format(min_profit_month, min_profit), file = f)

