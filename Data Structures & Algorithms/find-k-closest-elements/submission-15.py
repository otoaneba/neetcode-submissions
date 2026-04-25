class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        for loop or while loop until the r reaches end
            - while the window is less than k, evaluate if the current element at r is closer
                - if so, expand right
                - else, shrink from left
            - possible to miss some values to the right if we break early
        
        better to shrink from right to left to cover all elements where l = 0, r = len(arr)- 1
        do this while r - l + 1 less than k
        if |a-x| < |b-x| left is closer so shrink from right 
            decrement right 
        else (|a-x| >= |b-x| and a < b) right is closer so shrink from left
            increment left 
        
        after the while, return the arr[l:r]
        """

        l,r = 0, len(arr) - 1
        while r - l + 1 > k:
            if abs(arr[l] - x) <= abs(arr[r] - x):
                r -= 1
            else: 
                l += 1
        
        return arr[l:r+1]
