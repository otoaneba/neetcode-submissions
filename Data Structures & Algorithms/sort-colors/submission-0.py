class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # I'm given a list of numbers, which are either 0, 1, or 2, and I have to sort them in ascending order
        # I don't return anything, and I have to sort this in-place without a built-int library.

        # Will the list every be empty? Smallest size == 1
        # can I assume that I can use python?
        
        # I can't think of a way to brute force this, but i've seen similar patterns of sorting,
        # so I'd like to use that if I can.

        n = len(nums)

        for index in range(n - 2 // 2, -1, -1):
            self.heapify(nums, index, n)
        
        for end in range(n - 1, 0, -1):
            nums[0], nums[end] = nums[end], nums[0]
            self.heapify(nums, 0, end)

    def heapify(self, nums: List[int], i: int, heap_size: int):
        
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i

            if left < heap_size and nums[left] > nums[largest]:
                largest = left
            if right < heap_size and nums[right] > nums[largest]:
                largest = right
            
            if largest == i:
                return

            nums[i], nums[largest] = nums[largest], nums[i]
            i = largest