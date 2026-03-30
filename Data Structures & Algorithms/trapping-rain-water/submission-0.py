class Solution:
    def trap(self, height: List[int]) -> int:
        """
        given a list of non-negative integers, height, where each element height[i] represents
        the height of the bar, return an integer value taht represent the maximum area of
        water that can be trapped between the bars.


        will the height ever be empty?
        what are we trying to optimize? time or space? can I use extra space if optimizing for time?
        Am I allowed to sort? (assume not)
        can i use python and its built-in libraries when necessary?

        Input: height = [0,2,0,3,1,0,1,3,2,1]
        Output: 9

        because 203 -> 2, 31013 -> 2 + 3 + 2 = 7, 2+7 -> 9


        [0,2,0,3,1,0,1,3,2,1]
         l r
           l r
           l   r

     area = 2
        l = 0 -> 2
        r = 2 -> 0

        """
        maxLeft = []
        maxRight = []
        currMaxLeft = height[0]
        currMaxRight = height[len(height) - 1]
        for h in height:
            if h > currMaxLeft:
                currMaxLeft = h
            maxLeft.append(currMaxLeft)
        
        for h in reversed(height):
            if h > currMaxRight:
                currMaxRight = h
            maxRight.insert(0, currMaxRight)

        print(height)
        print(maxLeft)
        print(maxRight)
        
        res = 0
        for index, h in enumerate(height):
            minHeight = min(maxLeft[index], maxRight[index])
            trappedWater = minHeight - h
            if trappedWater > 0:
                res += trappedWater
        return res
