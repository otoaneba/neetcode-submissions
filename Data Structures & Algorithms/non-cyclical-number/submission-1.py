class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
    
        while n != 1:
            currSum = 0
            while n > 0:
                currSum += (n % 10) ** 2
                n = n // 10

            if currSum in seen:
                return False
            seen.add(currSum)
            n = currSum

        return True