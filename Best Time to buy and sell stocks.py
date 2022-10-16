#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv
'''
k = 2, prices = [3,2,6,5,0,3] 
buy on day 2 ie at price 2 then sell it at day 3 at price 6 ---->profit(6-2=4) ------------------->k=1
buy on day 5 and sell on day 6 so------------------------------> profit(3-0=3) ------------------->k=2
net profit = 4+3 = 7
'''


#level 2
from functools import lru_cache
class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(None)
        def check(ind,buy,n):
            if ind==n:
                return 0
            if (ind,buy) in dp:
                return dp[(ind,buy)]
            if buy:
                dp[(ind,buy)]=max(-prices[ind]+check(ind+1,0,n),check(ind+1,1,n))
            else:
                dp[(ind,buy)]=max(prices[ind]+check(ind+1,1,n),check(ind+1,0,n))
            return dp[(ind,buy)]
        dp={}
        return check(0,1,len(prices))
 #level 4
 class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp={}
        def check(ind,transaction):
            if ind==len(prices) or transaction == k*2:
                return 0
            if (ind,transaction) in dp: 
                return dp[(ind,transaction)] 
            if transaction%2==0:
                dp[(ind,transaction)]=max(-prices[ind]+check(ind+1,transaction+1),check(ind+1,transaction))
                return dp[(ind,transaction)]
            else:
                dp[(ind,transaction)]=max(prices[ind]+check(ind+1,transaction+1),check(ind+1,transaction))
                return dp[(ind,transaction)]
        return check(0,0)
    
    
