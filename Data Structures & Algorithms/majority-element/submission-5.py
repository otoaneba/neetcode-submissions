class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        majority = len(nums) / 2
        res = nums[0]
        for num in nums: 
            count[num] = count.get(num, 0) + 1

            if count[num] > len(nums) / 2:
                res = num
        return res


        
        
