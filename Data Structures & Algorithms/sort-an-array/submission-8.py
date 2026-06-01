class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def mergeSort(arr: List[int], l: int, r: int) -> List[int]:
            if l >= r:
                return

            m = (l + r) // 2
            mergeSort(arr, l, m)
            mergeSort(arr, m+1, r)
            merge(arr, l, m, r)
            return arr
        
        def merge(arr: List[int], l: int, m: int, r:int) -> List[int]:
            left, right = arr[l:m+1], arr[m+1:r+1]
            i, j, k = l, 0, 0

            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i += 1
            
            while j < len(left):
                arr[i] = left[j]
                j += 1
                i += 1
            
            while k < len(right):
                arr[i] = right[k]
                k += 1
                i += 1

        mergeSort(nums, 0, len(nums) - 1)
        return nums