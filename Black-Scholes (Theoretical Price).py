'''
Reference: https://www.macroption.com/black-scholes-excel/
'''


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# import library
import numpy as np
from scipy.stats import norm    # 從 Science Statistics 中引入常態分配進來



# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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



'''
(2024.11.02) 不知道為什麼 Visual Studio 不可以像其他的 IDE 一樣直接打一堆的 input 就可以順序的輸入資料進去
'''
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Testing
print('請輸入該選擇權之標的物價格($)')
Underlying = float(input())
65.24

print('請輸入該選擇權之履約價格($)')
Strike = float(input())
65.00

print("請輸入該選擇權之剩餘到期天數(Days)")
Days = int(input())
16

print("請問您輸入的到期天數是以日曆日(Calenders, 365 Days)或以交易日(Business, 260 Days)，請以英文回答")
Times = str(input())
Calenders
if Times == 'Calenders':
    Expiration = Days/365
elif Times == 'Business':
    Expiration = Days/260

print("請輸入該年利率(%)")
Interest = float(input())/100
1

print("請輸入該選擇權之標的物股利率(%)")
Dividend = float(input())/100
0

print("請輸入該選擇權之標的物波動率(%)")
Volatility = float(input())/100
39.55



# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Output
Call, Put = BS_Price(S=Underlying, K=Strike, t=Expiration, r=Interest, q=Dividend, sigma=Volatility)

