class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # phase 1: build max heap
        for index in range((n - 2) // 2, -1, -1):
            self.heapify(nums, index, n)

        # phase 2: repeat until sorted
        for end in range(n - 1, 0, -1):
            nums[0], nums[end] = nums[end], nums[0]

            self.heapify(nums, 0, end)
        return nums

    def heapify(self, nums: List[int], i: int, heap_size: int) -> None:
        while True:
            left = 2*i + 1
            right = 2*i + 2
            largest = i

            if left < heap_size and nums[left] > nums[largest]:
                largest = left
            if right < heap_size and nums[right] > nums[largest]:   
                largest = right
            
            if largest == i:
                return 
            
            nums[i], nums[largest] = nums[largest], nums[i]
            i = largest