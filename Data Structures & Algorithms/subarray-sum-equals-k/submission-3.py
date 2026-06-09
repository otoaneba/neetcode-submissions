class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {0:1}
        res = 0
        currSum = 0

        for num in nums:
            currSum += num
            if currSum - k in prefixSum:
                res += prefixSum[currSum - k]
            prefixSum[currSum] = prefixSum.get(currSum, 0) + 1
        
        return res