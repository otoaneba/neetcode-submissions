class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freqSet = set()
        for num in nums:
            if num not in freqSet:
                freqSet.add(num)
            else:
                return True
        return False