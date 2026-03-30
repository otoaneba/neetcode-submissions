class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # use element as key and index as value 
        seen = {}
        for index in range(len(nums)):
            if target - nums[index] not in seen:
                seen[nums[index]] = index
            else:
                return [seen[target - nums[index]], index]

        
    # {{3: 0}, }
    # return seen[3], currentIndex
    # [3,4,5,6]
    # target=7