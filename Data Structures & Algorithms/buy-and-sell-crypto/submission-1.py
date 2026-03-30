class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # curr_max_profit = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         if prices[j] > prices[i] and prices[j] - prices[i] > curr_max_profit:
        #             curr_max_profit = prices[j] - prices[i]
  
        # return curr_max_profit
        l, r = 0, 1
        max_profit = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                max_profit = max(max_profit, prices[r] - prices[l])
            else:
                print(prices[l], prices[r])
                l = r
            r += 1
        return max_profit