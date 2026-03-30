class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        We are given an array of integers (numbers) in ascending order, and a target. We must return 
        two indices in the list, [index1, index2], such that  the values of those 
        indices add up to target AND index1 < index2. We cannot use the same index twice.
        There will always be exactly one valid solution.

        We must use O(1) extra space.

        can i use python and the built-in library when/if necessary?
        the array will have at least 2 numbers, is that correct?
        will each element in the array fit into memory?
        will the array fit into memory?
        will the target fit into memory and would it be valid?
        what are we optimizing for? time or space?
        will every element be unique?


        Example 1:
        given [1,2,3,4] target=3, output should be [1,2] (1 indexed)
        given [2,3,4,6,2] target=4, output should be [1, 5] (1 indexed)

        solution 1:
        for each element, we can check every other element to get target. For this
        one, we have to make sure that we don't check for values where index[1] <= index2, since
        index1 must be less than index 1. time of n nlogn? space of O(1)

        two pointers checking each value since it's sorted, we can check if the sum 
        of two values are less than or greater than. If less, we move the left because 
        we are looking for a bigger sum. If the current sum is greater than the target, 
        we decrement the right pointer because we are looking for a target that is smaller.
        O(n) time, O(1) space.

        """
    #     [1,2,3,4] target=3
    #      l     r
    #      l   r   
    #      l r
                   
    # currSum = 0 -> 5 -> 4 -> 3
    #            l = 0 -> 0 -> 0
    #            r = 3 -> 2 -> 1
    #            l < r ? yes 
    #            l+=1, r+=1
    #            [1,2]
    #            # I'm going to use 0 indexed and add one at the end since 
    #            # it's easier for me to think in 0-indexed structure


    #     logic:
    #     initialize left and right with 0
    #     initalize currSum with 0
    #     while left < right
    #         get the sum of numbers[left] + numbers[right]
    #         if < target
    #             increment left by 1
    #         elif > target
    #             decrement right by 1
    #         else (equal)
    #             return [left+1, right+1]
        left = 0
        right = len(numbers)-1
        currSum = 0
        while left < right:
            currSum = numbers[left] + numbers[right]
            if currSum < target:
                left += 1
            elif currSum > target:
                right -= 1
            else:
                return [left+1, right+1]
        

