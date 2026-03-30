class Solution:
    def maxArea(self, heights: List[int]) -> int:
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

            if area > currArea:
                currArea = area
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return currArea


