class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        AAABABB

        freqMap = {}
        l,r = 0, 0
        maxFreq = 0

        for loop until right pointer reaches end:
            freqMap[s[r]] = freqMap.get(s[r], 0) + 1
            maxFreq = max(maxFreq, freqMap[s[r]])

            r - l + 1 - maxFreq <= k ?? 
                res = max(res, r - l + 1)
            
            otherwise
                while r - l + 1 - maxFreq > k:
                    freqMap[l] -= 1
                    l += 1
            res = max(res, r - l + 1)

        how do I make sure not to add the character AGAIN after I 
        increment the left pointer?

        currently, it only works because it assumes that only the
        right pointer moves forward. 


        """
        freqMap = {}
        l,r = 0, 0
        maxFreq = 0
        res = 0

        for r in range(len(s)):
            # 1. Expand
            freqMap[s[r]] = freqMap.get(s[r], 0) + 1
            maxFreq = max(maxFreq, freqMap[s[r]])

            # 2. Shrink if invalid
            while (r - l + 1) - maxFreq > k:
                freqMap[s[l]] -= 1
                l += 1
            
            # 3. Record (At this point, the window is guaranteed to be valid)
            res = max(res, r - l + 1)
        return res