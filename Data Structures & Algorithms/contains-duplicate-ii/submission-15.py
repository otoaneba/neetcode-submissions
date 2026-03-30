class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        return true such that nums[i] == nums[j] and abs(i - j) <= k otherwise return false.
        nums -> list of integers
        k -> integer

        will nums ever be empty?
        will k ever be less than 1? what if it's 0 or less?
        will nums always have valid elements?
        will k ever be longer than the length of nums? should return false
        will we have duplicate numbers?

        Input: nums = [1,2,3,1], k = 3
        Output: true

        Input: nums = [2,1,2], k = 1
        Output: false

        if length of nums is 1 and k = 0, return true
        if length of nums is 1 and k > 0, return false

        


        """
        if len(nums) == 1 and k == 0:
            return True
        if len(nums) == 1 and k > 0: 
            return False

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and abs(i - j) <= k:
                    return True
        
        return False