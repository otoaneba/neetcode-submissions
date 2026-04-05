class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        create a bucket array for len(nums), where each index represents the frequency since
        the nums array can contain elements with freq from 1 - n
        
        count frequencies with a dict or Counter

        create result array

        for each value in counter dict, add to bucket using the value of the freq dict as index

        iterate from last index from the bucket and fill in result array until k values are 
        inserted 

        
        """

        counter = Counter(nums)
        
        buckets = [[] for i in range(len(nums) + 1)]
        print(buckets)
        res = []

        print(counter)
        for num, count in counter.items():
            print(counter[count])
            buckets[count].append(num)
        
        for index in range(len(buckets)-1, 0, -1):
            
            for num in buckets[index]:
                res.append(num)

            if len(res) == k:
                return res
        
        
        
