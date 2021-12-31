import math
from scipy import stats 
def get_call_premium(ltp,strike,tm,vola):

    tm = tm/365
    d1 = (math.log(ltp/strike)+(tm*0.5*vola))/(vola*math.sqrt(tm)) 
    d2 = d1-vola*math.sqrt(tm)
    Nd1 = stats.norm.cdf(d1) 
    Nd2 = stats.norm.cdf(d2) 
    premium = ltp*Nd1 -strike*Nd2
    return int(premium) 
print(get_call_premium(ltp=35000 ,strike=35000 ,tm=1, vola=0.25)) # return 182 
print(get_call_premium (ltp=35000, strike=35500, tm=1, vola=0.25)) # return 32 
print(get_call_premium(ltp=35250, strike=35500, tm=1, vola=0.25)) # return 85
