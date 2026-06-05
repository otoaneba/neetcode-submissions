class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        res = []
        
        for num, value in count.items():
            if value > (len(nums) // 3):
                res.append(num)
        
        return res