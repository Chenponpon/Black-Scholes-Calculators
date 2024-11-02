'''
這邊的目的在於，要做一個簡單的應用程式，然後可以把 Black Scholes Model 中的選擇權理論價格以及 Implied Vol 算出來
Reference : https://www.macroption.com/black-scholes-excel/
'''


# --------------
# import library
import numpy as np
import tkinter as tk 
from scipy import optimize
from scipy.stats import norm    # 從 Science Statistics 中引入常態分配進來

# ------- 第一階段 : 基本款 Black Scholes Model 
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

# Components Function
def BS_Components(S, K, t, r, q, sigma):
    d1 = (np.log(S/K) + t*(r - q + 0.5*np.power(sigma, 2)))  /  (sigma*np.power(t, 0.5))
    d2 = d1 - (sigma*np.power(t, 0.5))
    discount_r = np.exp(-r * t)
    discount_q = np.exp(-q * t)
    return d1, d2, discount_r, discount_q

# Black Scholes Function
def BS_Price(S, K, t, r, q, sigma):
    d1, d2, discount_r, discount_q = BS_Components(S, K, t, r, q, sigma)
    Call_Price = S * discount_q * norm.cdf(d1) - K * discount_r * norm.cdf(d2)
    Put_Price = K * discount_r * norm.cdf(-d2) - S * discount_q * norm.cdf(-d1)
    return Call_Price, Put_Price

# ------- 第一階段 : Call Put Price 輸出
# Premium
Call, Put = BS_Price(Underlying, Strike, Expiration, Interest, Dividend, Volatility)
print(Call)
print(Put)





# ------- 第二階段 : 用最佳解去算出 Implied Volatility
# Implied Volatility (Call)
def Call_IV(S, K, t, r, q, Call):  

    def BS_Price(IV):
       d1, d2, discount_r, discount_q = BS_Components(S, K, t, r, q, IV)
       Call_Price = S * discount_q * norm.cdf(d1) - K * discount_r * norm.cdf(d2)
       return Call - Call_Price

    return optimize.brentq(BS_Price, 0.0001, 100, maxiter=1000)     #在Function(BS_Price)中，藉由改變該Function中的變數(IV)，自0.0001 到 100 這區間迭代 1000 次運算找出最小
# Implied Volatility (Put)
def Put_IV(S, K, t, r, q, Put):  

    def BS_Price(IV):
       d1, d2, discount_r, discount_q = BS_Components(S, K, t, r, q, IV)
       Put_Price = K * discount_r * norm.cdf(-d2) - S * discount_q * norm.cdf(-d1)
       return Put - Put_Price

    return optimize.brentq(BS_Price, 0.0001, 100, maxiter=1000)     #在Function(BS_Price)中，藉由改變該Function中的變數(IV)，自0.0001 到 100 這區間迭代 1000 次運算找出最小

Call_IV(S=53.2, K=55, t=18/365, r=0.01, q=0.02, Call=1.4)
Put_IV(S=53.2, K=55, t=18/365, r=0.01, q=0.02, Put=2)


