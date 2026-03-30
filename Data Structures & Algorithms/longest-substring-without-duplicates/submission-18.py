class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = set() 
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in freq:
                freq.remove(s[l])
                l += 1
            freq.add(s[r])
            res = max(res, r - l + 1)
        return res
