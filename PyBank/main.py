{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-2315.12\n",
      "86\n",
      "38382578.0\n",
      "1926159.0\n",
      "-2196167.0\n",
      "1170593.0\n",
      "Feb-2012\n",
      "-1196225.0\n",
      "Sep-2013\n"
     ]
    }
   ],
   "source": [
    "import csv\n",
    "\n",
    "import os\n",
    "\n",
    "#hw_name = (\"C:/Users/jarjar/Desktop/budget_data.csv\")\n",
    "hw_name = (\"Desktop/budget_data.csv\")\n",
    "\n",
    "\n",
    "max_profit = 0\n",
    "max_profit_month = \"\"\n",
    "min_profit = 0\n",
    "min_profit_month = \"\"\n",
    "total_months = 0\n",
    "total_profit = 0\n",
    "max_change = 0\n",
    "min_change = 0\n",
    "total_change = 0\n",
    "\n",
    "\n",
    "with open(hw_name, 'r') as csvfile:\n",
    "    csv_data = csv.reader(csvfile)\n",
    "    \n",
    "    #gets rid of header\n",
    "    next(csv_data)\n",
    "    \n",
    "    previous_profit = 0\n",
    "    first_month = True\n",
    "\n",
    "    for line in csv_data:\n",
    "        profit = float(line[1])\n",
    "        if first_month:\n",
    "            first_month = False\n",
    "        else:\n",
    "            change = profit - previous_profit\n",
    "            if max_change < change:\n",
    "                max_change = change\n",
    "            if min_change > change:\n",
    "                min_change = change\n",
    "            total_change += change\n",
    "        total_profit += profit\n",
    "        if max_profit < profit: #max profit\n",
    "            max_profit = profit\n",
    "            max_profit_month = line[0]\n",
    "        if min_profit > profit: #min profit\n",
    "            min_profit = profit\n",
    "            min_profit_month = line[0]\n",
    "        total_months += 1 #total months\n",
    "        previous_profit = profit\n",
    "\n",
    "\n",
    "\n",
    "average_change = round(total_change / (total_months - 1), 2)\n",
    "\n",
    "\n",
    "print(average_change)\n",
    "print(total_months)\n",
    "print(total_profit)\n",
    "print(max_change)\n",
    "print(min_change)\n",
    "print(max_profit)\n",
    "print(max_profit_month)\n",
    "print(min_profit)\n",
    "print(min_profit_month)\n",
    "\n",
    "with open('testfile.txt', 'w') as f:\n",
    "    print(\"Total Months: {}\".format(total_months), file = f)\n",
    "    print(\"Total Profit ${}\".format(total_profit), file = f)\n",
    "    print(\"Average Change: {}\".format(average_change), file = f)\n",
    "    #print(max_change, file = f)\n",
    "    #print(min_change, file = f)\n",
    "    print(\"Greatest Increase in Profits {} was ${}\".format(max_profit_month, max_profit), file = f)\n",
    "    print(\"Greatest Derease in Profits {} was ${}\".format(min_profit_month, min_profit), file = f)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
