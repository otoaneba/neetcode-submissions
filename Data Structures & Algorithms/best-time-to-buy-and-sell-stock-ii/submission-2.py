class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        currPrice = float('inf')
        for num in prices:
            currPrice = min(currPrice, num)
            if num > currPrice:
                res += num - currPrice
                currPrice = num
        return res