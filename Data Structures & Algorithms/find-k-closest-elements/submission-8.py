class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        I need to return the k closest integers to x in the array, arr. 

        k = 2
        x = 6
        [2, 4, 5, 8]  res  
         l  r         [0:1+1] 
         l.    r      [0:2+1] # if |r - x| is close to x than |l - x|, then we shift the window to the right by removing the left item.
            l.    r   [1:2+1] # if |r - x| is farther to x or same but r > l, than we take l as priority.

        k = 3
        x = 13
       [2, 4, 5, 8, 10, 11, 12, 15, 19, 21, 22]  res
        lr                                       [0:0+1] 
        l. r                                     [0:1+1]
        l     r                                  [0:2+1]
        l.       r                               [0:3+1] window too big. shrink
           l.    r                               [1:3+1] r-x still smaller than l-x, keep going
           l.       r                            [1:4+1] window too big. shrink
              l.    r                            [2:4+1] r-x still smaller than l-x, keep going
              l         r.                       [2:5+1] window too big. shrink
                 l      r                        [3:5+1] r-x still smaller than l-x, keep going
                 l.          r.                  [3:6+1] window too big. shrink
                     l.      r.                  [4:6+1] r-x still smaller than l-x, keep going
                     l.         r.               [4:7+1] window too big. shrink
                        l.      r                [5:7+1] r-x == l-x but arr[l] < arr[r] return arr[5:7+1]


        somewhere in the loop, we need to check whether l is closer to x than r. 
        If so, we've reached the optimal window. If right edge if farther than 
        the left edge, we shouldn't expand more as that will cause the window to 
        be farther than the target, x. 
        if |l - x| < |r - x| or (|l - x| == |r - x| and arr[l] < arr[r]) or r == len(arr) - 1
          return arr[l:r+1]
        
        if we need to shrink, we only need to increment l by 1


        """
        l = 0

        for r in range(len(arr)):
          while r - l + 1 > k:
            if abs(arr[l] - x) > abs(arr[r] - x):
              l += 1
            else:
              break
          
        return arr[l:l+k]
        


