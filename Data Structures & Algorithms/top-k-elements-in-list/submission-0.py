# can I use python and its built-in libraries?
# will the array be sorted?
# what are we optimizing for?
# can I use extra space to optimize?
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        arr = []
        for num, freq in counter.items():
            arr.append([freq, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res