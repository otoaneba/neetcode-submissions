class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        at any given time, we can look at a specific subarray to see if the sum of that 
        subarray is >= to the target. There's a technique we can use to dynamically shrink
        and expand a subarray (or window) based on a condition.
        we need:
            - two pointers: l and r 
            - a current sum inside that window
            - a res (length of window of the min size window at every iteration)
        
        target = 10, nums = [2,1,5,1,5,3]

        [2, 1, 5, 1, 5, 3]
        lr                  2
        l   r               3
        l.     r            8
        l.        r         9
        l.           r      14 greater than target. see if we can shrink 
        while currSum is >= target, save min and shrink left 
            l        r      12
               l.    r.     11
                  l  r      6.  too small now. stop shrinking and keep moving right pointer
                  l     r   9.  right pointer at end. exit
        """
        l = 0
        currSum = 0
        res = float('infinity')

        for r in range(len(nums)):
            currSum += nums[r]
            while currSum >= target: # add equal to because we need to save the subarray length whtn its equal to the target 
                res = min(res, r - l + 1)
                currSum -= nums[l]
                l += 1
            

        return 0 if res == float('infinity') else res
