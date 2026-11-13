class Solution(object):
    def maxProfit(self, prices):
        maxP= 0 
        l,r=0,1 

        while r<len(prices):
            if prices[r]>prices[l]:
                profit = prices[r]-prices[l]
                maxP=max(profit,maxP)
            elif prices[l]>prices[r]:
                l=r
            r+=1

        return maxP
        