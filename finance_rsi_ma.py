#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 04:24:28 2018

@author: ahanmr
"""

"""
We want to add historical data to our machine learning models to make better predictions, but adding lots of historical time steps is tricky. Instead, we can condense information from previous points into a single timestep with indicators.

A moving average is one of the simplest indicators - it's the average of previous data points. This is the function talib.SMA() from the TAlib library.

Another common technical indicator is the relative strength index (RSI).
The n periods is set in talib.RSI() as the timeperiod argument.
"""

import matplotlib.pyplot as plt
import pandas as pd
import talib
df1=pd.read_csv("/home/ahanmr/Desktop/Hackathon/individual_stocks_5yr/AAPL_data.csv")
df2=pd.read_csv("/home/ahanmr/Desktop/Hackathon/individual_stocks_5yr/AAL_data.csv")
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
plt.show()
#plt.show()
features=['close_pct']
# simple moving average and relative strength index
for i in [14,30,50,200]:
    df1["sma"+str(i)]=talib.SMA(df1["close"],timeperiod=i)/df1['close']
    df1["rsi"+str(i)]=talib.RSI(df1["close"],timeperiod=i)
    features=features+["sma"+str(i),"rsi"+str(i)]

print(features)

df1=df1.dropna()
#print(df1)
features_names=df1[features]
targets=df1["5d_future_close_pct"]
feat_targ_df = df1[['5d_future_close_pct'] + features]
corr=feat_targ_df.corr()
print(corr)

import seaborn as sns
sns.heatmap(corr,annot=True)
plt.show()

























