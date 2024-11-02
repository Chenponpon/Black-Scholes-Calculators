'''
Reference: https://www.macroption.com/black-scholes-excel/
'''


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# import library
import numpy as np
from scipy.stats import norm    # 從 Science Statistics 中引入常態分配進來
from scipy import optimize      # 這邊多引入最佳化工具，用來做規劃求解用的



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
# Implied Volatility (Call)
def Call_IV(S, K, t, r, q, Call):  

    def BS_Price(IV):
       d1, d2, discount_r, discount_q = BS_Components(S, K, t, r, q, IV)
       Call_Price = S * discount_q * norm.cdf(d1) - K * discount_r * norm.cdf(d2)
       return Call - Call_Price

    return optimize.brentq(BS_Price, 0.0001, 100, maxiter=1000, full_output=True)     #在Function(BS_Price)中，藉由改變該Function中的變數(IV)，自0.0001 到 100 這區間迭代 1000 次運算找出最小
# Implied Volatility (Put)
def Put_IV(S, K, t, r, q, Put):  

    def BS_Price(IV):
       d1, d2, discount_r, discount_q = BS_Components(S, K, t, r, q, IV)
       Put_Price = K * discount_r * norm.cdf(-d2) - S * discount_q * norm.cdf(-d1)
       return Put - Put_Price

    return optimize.brentq(BS_Price, 0.0001, 100, maxiter=1000, full_output=True)     #在Function(BS_Price)中，藉由改變該Function中的變數(IV)，自0.0001 到 100 這區間迭代 1000 次運算找出最小


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

print("請輸入試算之 Call 目前價格($)")
Call_Price = float(input())
1.4

print("請輸入試算之 Put 目前價格($)")
Put_Price = float(input())
2


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Output
Call_IV_Output = Call_IV(S=Underlying, K=Strike, t=Expiration, r=Interest, q=Dividend, Call=Call_Price)
BS_Price(S=Underlying, K=Strike, t=Expiration, r=Interest, q=Dividend, sigma=Call_IV_Output[0])[0]      # 以現在的價格規劃求解出 IV 之後，再帶回 Black Scholes 可以得出 Call Price
Call_Price      # 這就是原本代入的 Call Price

Put_IV_Output = Put_IV(S=Underlying, K=Strike, t=Expiration, r=Interest, q=Dividend, Put=Put_Price)
BS_Price(S=Underlying, K=Strike, t=Expiration, r=Interest, q=Dividend, sigma=Put_IV_Output[0])[1]      # 以現在的價格規劃求解出 IV 之後，再帶回 Black Scholes 可以得出 Put Price
Put_Price      # 這就是原本代入的 Put Price
