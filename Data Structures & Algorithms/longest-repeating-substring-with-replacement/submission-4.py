class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
                  r 
        A A A B A B B 
        l

        {A:4, B:2} 
        

        r - l + 1 - maxFreq <= k -> res = max(res, r - l + 1)
        if not valid, shift l 
        freqMap
        left pointer (r moving automatically)
        res = 0 

        """

        freqMap = {}
        l = 0
        maxFreq = 0
        res = 0

        for r in range(len(s)):
            freqMap[s[r]] = freqMap.get(s[r], 0) + 1
            maxFreq = max(maxFreq, freqMap[s[r]])

            while r - l + 1 - maxFreq > k:
                freqMap[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res