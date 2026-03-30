class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        largestCount = nums[0]
        for value in nums:
            if value not in counter:
                counter[value] = 1
            else:
                counter[value] += 1
                if counter[value] > counter[largestCount]:
                    largestCount = value
        
        return largestCount