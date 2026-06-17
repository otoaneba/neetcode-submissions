class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        l = 0
        while l < len(word1) and l < len(word2):
            res += word1[l]
            res += word2[l]
            l += 1
        
        while l < len(word1):
            res += word1[l]
            l += 1
        
        while l < len(word2):
            res += word2[l]
            l += 1
        
        return res