class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        """
        i i+1 to len(nums) - 1
        but make sure i > 0 and i-1 != i
        if so, keep incrementing i
        need a res[] 
        for every iteration, if we find a triplet, add [nums[i], nujms[l], nums[r]] into res
        """
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            l, r = i+1, len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    
                    
                    while l < r and nums[l] == nums[l+1]:
                            l += 1
                    while l < r and nums[r] == nums[r-1]:
                            r -= 1
                    l += 1
                    r -= 1
        return res