class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j]>prices[i]:
                    maxm=prices[j]-prices[i]
                    if maxm>m:
                        m=maxm
        return m

