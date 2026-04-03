class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        heap sort:
        heapify first

        then, swap first element with last, and heapify every other element start 
        with the end element


        heapify(arr, index, heap_size):
            define left and right and largest

            check if left is > than largest and left is within heap_size 
                largest = left
            check if right is > than largest and left is within heap_size 
                largest = right
            check if largest == i, then the parent is at the correct postion
                return
            
            swap arr[largest], arr[i] = arr[i], arr[largest]
                return arr
        
        """
        n = len(nums)

        for i in range(n - 2 // 2, -1, -1):
            self.heapify(nums, i, n)
        
        for end in range(n - 1, 0, -1):
            nums[0], nums[end] = nums[end], nums[0]
            self.heapify(nums, 0, end)
        
    def heapify(self, arr: List[int], i: int, heap_size: int):
        while True:
            left, right, largest = 2*i + 1, 2*i + 2, i

            if left < heap_size and arr[left] > arr[largest]:
                largest = left
            if right < heap_size and arr[right] > arr[largest]:
                largest = right
            
            if largest == i:
                return
            
            arr[largest], arr[i] = arr[i], arr[largest]
            i = largest
            