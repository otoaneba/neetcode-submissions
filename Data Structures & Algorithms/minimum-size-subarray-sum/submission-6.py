class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        

        """

        l = 0
        res = float('infinity')
        currSum = 0
        for r in range(len(nums)):
            currSum += nums[r] # why would I need to do this first?
            while currSum >= target:
                res = min(res, r - l + 1)
                currSum -= nums[l]
                l += 1
        
        return 0 if res == float('infinity') else res
            
