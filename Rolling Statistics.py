# Preparation
import matplotlib.pyplot as plt
import pandas as pd
from pandas import read_csv

# User Input
goog = pd.read_csv(open('GOOG.csv', encoding = 'UTF-8'))
i = int(input("Please enter a window size, >1, <252: "))

if i<=0 or i > 251:
    print("Invalid import! Please enter an integer in the range of [1,251].")
else:
    print("The window size is ", i)

# Rolling Window
newgoog = goog.rolling(window = i )
mean = newgoog['Adj Close'].mean()
median = newgoog['Adj Close'].median()
std = newgoog['Adj Close'].std()
_max = newgoog['Adj Close'].max()
_min = newgoog['Adj Close'].min()
upper = mean + std
lower = mean - std
_range = _max - _min

# Plot
x = goog['Date']
p = mean
q = median
r = upper
s = lower
t = _max
u = _min
v = goog['Adj Close']
p, = plt.plot(x , p)
q, = plt.plot(x , q)
r, = plt.plot(x , r)
s, = plt.plot(x , s)
t, = plt.plot(x , t)
u, = plt.plot(x , u)
v, = plt.plot(x , v)
plt.legend([p,q,r,s,t,u,v],('Mean','Median','Upper Bound','Lower Bound','Max','Min','Adj Close'))
plt.xticks(range(len(x))[::50], x[::50], rotation='30')
plt.xlabel('Date')
plt.ylabel('Adj Close')
plt.show()