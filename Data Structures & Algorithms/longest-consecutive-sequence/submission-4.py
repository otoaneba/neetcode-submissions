class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        values = set()
        for num in nums:
            values.add(num)
        
        startSeq = {}
        for num in values:
            if num - 1 not in values:
                startSeq[num] = 0
        
        print(startSeq)
        for num in startSeq:
            count = 1
            nextValue = num+1
            # while nextValue in values:
            #     count += 1
            #     nextValue += 1
            for n in range(num, num+len(nums)):
                if n+1 not in values:
                    break
                count += 1
        
            startSeq[num] = count
        return max(startSeq.values())



            