class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        values = set()
        for num in nums:
            values.add(num)
        
        startSeq = {}
        for value in values:
            if value - 1 not in values:
                startSeq[value] = 0
        
        for start in startSeq:
            count = 1
            nextValue = 1
            while start + nextValue in values:
                print(start + count)
                nextValue += 1
                count += 1
            startSeq[start] = count
            
        return max(startSeq.values())
