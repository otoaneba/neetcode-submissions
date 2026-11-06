class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def mergeSort(arr: List[int], L: int, R: int) -> List[int]:
            if L >= R:
                return
            M = (L + R) // 2
            mergeSort(arr, L, M)
            mergeSort(arr, M+1, R)
            merge(arr, L, M, R)
            return arr

        def merge(arr: List[int], L: int, M: int, R: int) -> None:
            left, right = arr[L:M+1], arr[M+1:R+1]
            i, j = 0, 0
            k = L

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    k += 1
                    i += 1
                else:
                    arr[k] = right[j]
                    k += 1
                    j += 1
            
            while i < len(left):
                arr[k] = left[i]
                k += 1
                i += 1
            while j < len(right):
                arr[k] = right[j]
                k += 1
                j += 1

        mergeSort(nums, 0, len(nums) - 1)
        return nums