class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        I'm given a array of integers, where every ith element represents a height. I have to return
        the most amount of water (area) that this array can hold. I have to return an integer, the array will
        have a length of at least 2, and each element can be 0 up to 1000.
        """

        """
        - can I use python and its libraries? yes, yes
        - what are we optimizing for ? If for time, can I use extra space? Time, yes
        - Will the height be negative? Will the height always fit into memory? yes, [0, 1000]
        - will the array every be empty? No - at least 2
        - 
        """

        """
        I'm thinking about using two pointers here because we'll have to move pointers
        depending on the height of each element, and having control over two pointers 
        would be easier than a automatic loop (like a for loop).

        I'm also thinking we can move outward to inward and saving each area in a set, and 
        i say area because we're essentially trying to get the biggest area here. That solution
        I think might take O(2n) where we get all the possible areas in one pass, then go through
        the map to find the biggest area.
        
        ok so length is not the number of elements. So an array of length 8 would start off with 
        a container length of 7 because two elements make up length of 1.
        
        """
                           
        # [1,7,2,5,4,7,3,6]
        #  l             r                
        #    l           r
        #    l         r 
        #    l       r
        #      l     r
        #        l   r
        #          l r
        # len =    7 -> 6 ->  5 ->  4 ->  3 -> 2 -> 1 length = right - left
        # height = 1 -> 6 ->  3 ->  7 ->  2 -> 5 -> 4 height = min(heights[l], heights[r])
        # area =   8 -> 36 -> 15 -> 28 -> 6 -> 10-> 4 area = length * height

        # logic:
        # create left and right
        # while left is not right, do the following
        #     get length
        #     get height
        #     get area
        #     is the area greater than the current area? save it.
        #     is the height at i less than or equal height at r? 
        #         move left
        #     else (the height at r less than height at l?)
        #         move right
        
        # return area
        left = 0
        right = len(heights)-1
        currArea = 0

        while left != right:
            length = right - left
            height = min(heights[left], heights[right])
            area = length * height
            # print(length, height, currArea, area)

            if area > currArea:
                currArea = area
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return currArea


