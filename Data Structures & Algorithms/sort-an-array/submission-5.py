class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        """
        1. divide by splitting the array into two - left and right
        2. recursively run step 1 until the array has a single value
        3. merge the left and right

        left arr ->  [left : middle]
        right arr -> [middle: right]
        merge(left arr, right arr)

        merge:
        # create temp array for left and right 
        L, R = arr[l : m + 1], arr[m + 1, r + 1]
        let i = 0 be the index in arr
        let j = 0 be the index in L arr
        let k = 0 be the index in R arr

        while j less than length of L arr AND k less than length of R arr
            if L[j] less than or equal to R[k]
                arr[i] = L[j]
                j += 1
            else: (R[k] is less)
                arr[i] = R[k]
                k += 1
            i += 1
        
        L arr or R arr may still be populated, so go through both

        while j < length of L:
            arr[i] = L[j]
            j+= 1
            i += 1
        
        while k < length of R:
            arr[i] = R[k]
            k += 1
            i += 1
        """
        def merge(arr: List[int], l: int, m: int, r: int) -> List[int]:
            left, right = arr[l:m+1], arr[m+1:r+1]
            i, j, k = l, 0, 0

            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else: # (R[k] is less)
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
        
        def mergeSort(arr: List[int], l: int, r: int) -> List[int]:
            if l == r:
                return arr

            m = (l + r) // 2
            mergeSort(arr, l, m)
            mergeSort(arr, m + 1, r)
            merge(arr, l, m, r)
            return arr

        return mergeSort(nums, 0, len(nums) - 1)    