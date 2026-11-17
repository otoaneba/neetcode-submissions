class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #1 [1,   2,   4,   6] 1      


         #  1.   1.   2.   8  rProduct

         # 48    24    6    1 lProduct


         # 48  24   12  8  

        rProduct = 1
        lProduct = 1
        res = []
        for n in nums:
            res.append(rProduct)
            rProduct *= n
        
        for i in range(len(res)-1, -1, -1):
            res[i] *= lProduct
            lProduct *= nums[i]
        
        return res
            
        
        
