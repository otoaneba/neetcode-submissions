class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        bucket = [[] for _ in range(10 ** 4)]
        result = []

        for key, value in c.items():
            (bucket[value]).append(key)

        for item in reversed(bucket):

            if len(item) > 0:
                j = 0
                while len(result) <= k and j < len(item):
                    result.append(item[j])
                    j += 1
                    
                    if len(result) == k:
                        return result
        
