class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        current_product = 1
        products = []
          
        for num in nums:
            products.append(current_product)
            current_product *= num
        
        current_product = 1
        for i in reversed(range(len(nums))):
            products[i] *= current_product
            current_product *= nums[i]
        return products

        
