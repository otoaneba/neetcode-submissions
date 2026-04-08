class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currSum = 0
        prefix = {0:1}
        res = 0

        for num in nums:
            currSum += num
            if currSum - k in prefix:
                res += prefix[currSum - k]
            prefix[currSum] = prefix.get(currSum, 0) + 1
        
        return res