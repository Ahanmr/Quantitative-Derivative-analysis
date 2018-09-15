#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 21:16:14 2018

@author: ahanmr
"""

import matplotlib.pyplot as plt
import pandas as pd
df1=pd.read_csv("AAPL_data.csv")
df2=pd.read_csv("AAL_data.csv")
# Plot the Adj_Close columns

df1['close'].plot(label='AAP')
df2['close'].plot(label='AAL')
plt.show()
# Histogram of the daily price change percent of Adj_Close for AAPL and AAL
#Use subplots for above to show both plots

plt.subplot(2,1,1)
df1["close"].pct_change().plot.hist(bins=50)
plt.xlabel("AAPL")

plt.subplot(2, 1, 2)
df2["close"].pct_change().plot.hist(bins=50)
plt.xlabel("AAL")
plt.show()
#10 days future based on shifting by 10 days
df1['5d_future_close']=df1['close'].shift(-10)
df1['5d_future_close_pct']=df1['5d_future_close'].pct_change(10)
df1['close_pct']=df1['close'].pct_change(10)
corr=df1[['close_pct','5d_future_close_pct']].corr()
print(corr)
plt.subplot(2,1,1)
plt.scatter(df1['close_pct'],df1['5d_future_close_pct'])

df2['5d_future_close']=df2['close'].shift(-10)
df2['5d_future_close_pct']=df2['5d_future_close'].pct_change(10)
df2['close_pct']=df2['close'].pct_change(10)
corr=df2[['close_pct','5d_future_close_pct']].corr()
print(corr)
plt.subplot(2,1,2)
plt.scatter(df2['close_pct'],df2['5d_future_close_pct'])
#plt.show()








#plt.clf()







