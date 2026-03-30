class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        [2,1,5,1,5,3] sum. res
         l r          3     0    
         l   r        8     0
               r      9     0
         l       r    14    5
           l     r    12    4
             l   r    11    3
               l r    6     3
               l   r  9     3      

        start with:
          l,r = 0, 1 
          res = 0
          sum = 0
        
        while the right pointer reaches end
          add values at l and r to sum
          if the sum is smaller than target
            increment r
          elif the sum is bigger than or equal to target
            get the min of the current subarray length and the previously saved length   

        """
        # if len(nums) == 1 and nums[0] >= target:
        #   return 1
        # elif len(nums) == 1 and nums[0] < target:
        #   return 0
        
        # l, r = 0, 1
        # currSum = 0
        # res = float("inf")
        
        # while r < len(nums):
        #   if currSum < target:
        #     currSum += nums[l] + nums[r]
        #     r += 1
        #   else:
        #     res = min(res, r - l + 1)
        #     currSum -= nums[l]
        #     l += 1
        
        # return 0 if res == float("inf") else res

        l = 0
        currSum = 0
        res = float("inf")

        for r in range(len(nums)):
          currSum += nums[r]

          while currSum >= target:
            res = min(res, r - l + 1)
            currSum -= nums[l]
            l += 1
        
        return 0 if res == float("inf") else res
            

          
        