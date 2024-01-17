class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        maxProfit=0
        if len(prices)<=1:
            return 0
        for r in range(1,len(prices)):
            profit=prices[r]-prices[l]
            maxProfit=max(maxProfit,profit)
            if prices[r]<prices[l]:
                l=r
                r+=1
        return maxProfit
