class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, num in enumerate(nums):
            value = target - num
            if value in seen:
                return [seen[value], index]
            else:
                seen[num] = index
        