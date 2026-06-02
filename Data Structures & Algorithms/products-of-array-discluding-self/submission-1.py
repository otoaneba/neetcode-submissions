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
            if i == 0:
                res.append(product)
            else:
                product *= nums[i-1]
                res.append(product)
        
        product = 1
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums) - 1:
                continue
            else:
                product *= nums[i+1]
                res[i] = res[i] * product
        
        return res
