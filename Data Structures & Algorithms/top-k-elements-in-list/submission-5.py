class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        why not nested loop?

        why not use Set?

        why not use Map?

        we use frequency as the bucket index, and since the max 
        frequency of a value in the nums array is len(nums), we
        need the size of the bucket list to be len(nums). But
        since python is 0-indexed, we need to allocate an extra 
        space, so we +1, resulting in len(nums) + 1
        """
        count = Counter(nums)
        freq = [[] for i in range(len(nums) + 1)]

        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res






