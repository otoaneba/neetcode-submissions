class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_max_profit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] > prices[i] and prices[j] - prices[i] > curr_max_profit:
                    curr_max_profit = prices[j] - prices[i]
  
        return curr_max_profit