class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        i'm given a list of integers, prices, where prices[i] is the price of the stock on the ith day.

        I can choose to buy a stock at any day and sell it in the future. 

        Return the maximum amount of profit I can make. I can choose not to buy.


        will the prices every be empty?
        will the prices be sorted?
        I don't think I can sort them, correct? because that'll change the date.
        will the values always be valid?
        are we optimizing for time or space? can I use extra space 


        Input: prices = [10,1,5,6,7,1]
        Output: 6

        Input: prices = [10,8,7,5,2]
        Output: 0

        [1,2,3,4,5]

        [2,3,1,4,1,5]
        - once left is at 2 and right is at 1, do we set left at right or decrement left once?
        - finish one thought process first before talking about new thought process

        """

        # currMax = 0
        # for i in range(len(prices)):

        #     for j in range(i+1, len(prices)):
        #         currMax = max(currMax, prices[j] - prices[i]);

        # return currMax

        buy = 0
        sell = 1
        currMax = 0
        # for i in range(len(prices)):
        #     if prices[sell] < prices[buy]:
        #         buy = sell
        #         sell = buy + 1
        #     elif prices[sell] > prices[buy]:
        #         sell += 1
        #     currMax = max(currMax, prices[sell] - prices[buy])
        # print(currMax)

        # I was able to figure out that
        # "If the price at r is lower, then r becomes the new l because a cheaper buying price is always better."
        # but was not confident enough nor wasn't 100% sure.. 

        # I need to understand the closing condition is when the SELL pointer reaches the end.
        # why does the BUY (the left pointer) not need to reach? Is there a possibility that 
        # there is a cheaper day in the future? No, because my logic would handle that.

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                currMax = max(currMax, prices[sell] - prices[buy])
            else:
                buy = sell
            sell += 1
        return currMax

