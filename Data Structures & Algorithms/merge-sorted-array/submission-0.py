class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        nums1 = [10,20,20,40,0,0], m = 4, nums2 = [1,2], n = 2

        [10,20,20,40,0,0]
        [1,20, 20, 40, 0, 0] 

        2 - 0 = 2  2 - 2 = 0 -> first index of swappable 0
        6 - 4 = 2  6 - 2 = 4 -> first index of swappable 0

        compare i and i - 1 
        """
        index = 0
        while index < len(nums2):
            nums1[m] = nums2[index]
            m += 1
            index += 1
        nums1.sort()
        return nums1 
        