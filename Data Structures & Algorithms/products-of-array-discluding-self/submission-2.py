class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        [1,2,4,6]

        [1, 1, 2, 8]
        
        48, 24, 6, 1

        """
        res = []
        product = 1
        for i in range(len(nums)):
            res.append(product)
            product *= nums[i]
        
        product = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * product
            product *= nums[i]
        
        return res
