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

        O(n)
        
        [10,9,5,11,1,1]
         b  s
            b.s
              b s
        """

        currMax = 0
        for i in range(len(prices)):

            for j in range(i+1, len(prices)):
                currMax = max(currMax, prices[j] - prices[i]);

        return currMax
