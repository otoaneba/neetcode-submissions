class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        return the maximum profit I can make. 
        prices -> integer list where prices[i] is the price of neetcoin on the ith day. I can choose to buy at any day and sell at any different and future day. 

        for every ith day, check every other future day and calculate the price. save the max, and after iterating every item, return the max -> O(n^2)


        """
        # we cannot buy and sell on the same day, so if the prices length is 1, we cannot make a profit
        if len(prices) == 1: 
            return 0
        
        l,r = 0, 1
        maxProfit = 0
        for r in range(1, len(prices)):
            if prices[r] > prices[l]:
                maxProfit = max(maxProfit, prices[r] - prices[l])
            else: 
                l = r
        return maxProfit
            
