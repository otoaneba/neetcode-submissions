class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        for each value in nums, we can add every other value. The minimum amount of values
        where the sum is equal or greater than the target is the result. 

        res is the length, j - i + 1
        currSum is the current sum, where it's reset every ith iteration
        """
        
        res = float('infinity')
        for i in range(len(nums)):
            currSum = 0

            for j in range(i, len(nums)):
                currSum += nums[j]
                if currSum >= target:
                    res = min(res, j - i + 1)
                    break
    
        return 0 if res == float('inf') else res
                