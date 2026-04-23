class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        [2, 4]


        [2,4,5,8] x=6
        1. what to do when the res arr is empty
            - len(arr) is not >= k, so res is now arr[l:r+1]
            - res is now [2]
        2. what to do when the res arr len is < k
            - len(arr) is not >= k, so res is now arr[l:r+1]
            - re is now [2, 4]
        3. what to do if the arr len is == k
            - determine if the new element at r is closer than first element at l 
                - |6 - 2| > |6 - 5| -> add 5 and remove 2 
                - increment l
                - res is now [4, 5]
        4. what to do if the arr len is == k
            - determine if the new element at r is closer than first element at l
                - |6 - 4| < |6 - 8| -> don't add new element at r
                - return because element greater than (since arr is sorted) current r will always be farther than l 
        
        prereq:
        for loop with r indexing from 0 to len(arr)
        l pointer init to 0
        res with empty arr

        performance:
        O(n) time
        O(m) space where m is size of k
        """
        
        l = 0
        res = []

        for r in range(len(arr)):
            if len(res) == k:
                # first element of res is closer to x than current element at r
                if abs(arr[l] - x) < abs(arr[r] - x) or (abs(arr[l] - x) == abs(arr[r] - x) and arr[l] < arr[r]):
                    return arr[l:r]
                # current element at r is closer to x than first element of res
                elif abs(arr[l] - x) > abs(arr[r] - x) or (abs(arr[l] - x) == abs(arr[r] - x) and arr[l] >= arr[r]):
                    l += 1
                    res = arr[l:r+1]
            else:
                res = arr[l:r+1]
        return res