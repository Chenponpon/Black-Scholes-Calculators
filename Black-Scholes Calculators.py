'''
這邊的目的在於，要做一個簡單的應用程式，然後可以把 Black Scholes Model 中的選擇權理論價格以及 Implied Vol 算出來
'''
# import library
import numpy as np
import tkinter as tk 
from scipy.optimize import linprog  # 從 Science Python 中引入線性規劃求解
from scipy.stats import norm    # 從 Science Statistics 中引入常態分配進來


# Black Scholes Model 
# -------
# initial
Underlying = 65.24
Strike = 65
Volatility = 0.3955
Interest = 0.01
Dividend = 0.00
Days = 16

Times = 'Calender'
if Times == 'Calender':
    Expiration = Days/365
elif Times == 'Trading':
    Expiration = Days/260

# ----------
# components 
d1 = (np.log(Underlying/Strike) + Expiration*(Interest - Dividend + 0.5*np.power(Volatility, 2)))  /  (Volatility*np.power(Expiration, 0.5))
d2 = d1 - (Volatility*np.power(Expiration, 0.5))

compound_div = np.exp(-Dividend * Expiration)
compound_int = np.exp(-Interest * Expiration) 


# -------
# Premium
Call = Underlying * compound_div * norm.cdf(d1) - Strike * compound_int * norm.cdf(d2)
Put = Strike * compound_int * norm.cdf(-d2) - Underlying * compound_div * norm.cdf(-d1)