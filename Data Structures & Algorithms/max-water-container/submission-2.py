class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        [1,7,2,5,4,7,3,6]

        - we need the area by calculating the min height * length (min height because water can only be held with lower wall)
        - length can be obtained by r - l 
        - height can be obtained by max(heights[l], heights[r])
        - we can start with l at index 0, and right at index len(heights) - 1
        - for every iteration we save the current max area
        - we have to move l or r each iteration. Since we want to maximize area, move the smaller 
            - move l if l is smaller than r
            - move r if r is smaller than l 
            - move l if height[l] == height[r] (arbitrary)
        - keep doing this until l < r
        - to begin, we need
            1. l and r both initialized to 0
            2. the area initialized to 0 
        
        [1, 7, 2, 5, 4, 7, 3, 6]. length area. currMax
         l                    r.    7.     7.     7
            l                 r.    6.     36.    36
            l              r        5.     21     36
            l           r           4.     28.    36
               l.       r           3.     6      36
                  l.    r           2      10.    36
                     l. r           1.     4      36
        """
        currMax = 0
        l, r = 0, len(heights) - 1

        while l < r:
            length = r - l
            area = min(heights[l], heights[r]) * length
            currMax = max(currMax, area)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return currMax