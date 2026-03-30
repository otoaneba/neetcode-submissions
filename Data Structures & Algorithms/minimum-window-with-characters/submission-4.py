class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        return the longest substring that includes all characters of t (including duplicates) in s. If no such string exists, return an empty string.

        s = "O U Z O D Y X A Z V", t = "XYZ"
            lr
               lr 
                 lr 
                       l r 
                       l  r 
                       l.    r
                      
            X U P O D Y X A Z V
            lr
            l.r 
            l.  r
            l.    r
            l.      r
            l         r  < X satisfied, Y satisfied
            l           r  < X surplus, Y satisfied. Since X surplus and not match complete, move left until it reaches any character inside t(Y)
                      l r. < X satisfied, Y satisfied.
                      l   r < X satisfied, Y satisfied
                      l     r < X satisfied, Y satisfied, Z satisfied. return YXAZ or s[l:r+1]

            - how do we determine which X is closer to the Y? need index and calculate current index - Y vs saved X's index - Y, but how do we know  
            - how do we move the left pointer so that it's at the most recent substring character(Y)? -> we move until we reach any character inside t
            - "match" has to be the number of unique characters
            - freqMap with alphabet array, where each index represent the count of the letter
            - need a left pointer starting at 0
            - right pointer can be moving automatically
            - use a while loop to move left pointer 
          

          X U Z O D Y X A Z V
          lr. < X satisfied
          l r
          l.  r   < X and Z satisfied
          l.    r
          l.      r
          l.        r. < X, Z, Y satisfid. But there might be more, so we move left pointer until the next match
              l.    r
              l.      r. < X surplus, so we move left pointer until the next match
                    l r
                    l.  r
                    l.    r  < X, Z, Y satisfied. 

            - how do we return the result? slicing the array with [l:r] ? or saving the best match each iteration, like "XUZODY" -> "ZODYX"
            - if using [l:r].. then we may need explicit right pointer, but if saving strings, we don't. Let's save strings

        we need:
        freqMap = [0] * 26
        l = 0
        res = ""

        base case:
        if length of t is longer than s, it's impossible since longer string cannot be a substring of a shorter string
        if length of s == length of t, then we just check if s == t. if identical, return s

        setup: 
        create freqMap by going through s and counting frequency of all unique characters in 
        
        
        1. Build frequency map for 2
          [0]*26 -> iterate t and increment += 1 for each character.
        2. Use a sliding window technique.
        3. Match is the length of freqT because we want the count for each unique character to match. We check against another frequency map, the sliding window. 
        4. We shrink the window if match === need but haven't reached the end OR we have a surplus of a character.
        5. We keep track of two result -> resLen, res = [l,r]
        
        
        """
        freqT = Counter(t)
        window = {}
        l = 0
        res = [-1,-1]
        resLen = float("infinity")
        matches = 0
        need = len(freqT)

        for r in range(len(s)):
          window[s[r]] = window.get(s[r], 0) + 1

          if s[r] in window and window[s[r]] == freqT[s[r]]:
            matches += 1
            
            while matches == need:
              # res = [l, r] # how do we save the shorter substring indices?
              # resLen = min(resLen, r - l + 1)
              if r - l + 1 < resLen:
                res = [l, r]
                resLen = r - l + 1
              
              window[s[l]] -= 1
              if s[l] in freqT and window[s[l]] < freqT[s[l]]:
                matches -= 1
              l += 1
        l, r = res
        return s[l: r + 1] if resLen != float("infinity") else ""






        