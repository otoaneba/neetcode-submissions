class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefixSum = 0
        oldSum = {0: 1}

        for num in nums:
            prefixSum += num
            if prefixSum - k in oldSum:
                res += oldSum[prefixSum - k]
            oldSum[prefixSum] = oldSum.get(prefixSum, 0) + 1
        return res