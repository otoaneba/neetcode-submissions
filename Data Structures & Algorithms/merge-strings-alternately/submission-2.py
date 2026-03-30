class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        # longerString = max(len(word1), len(word2))
        # for i in range(longerString):
        #     if i > len(word1) - 1:
        #         res += word2[i:]
        #         return res
        #     if i > len(word2) - 1:
        #         res += word1[i:]
        #         return res
        #     res += word1[i]
        #     res += word2[i]
        # return res
        index = 0
        while index < len(word1) and index < len(word2):
            res += word1[index]
            res += word2[index]
            index += 1
        res += word1[index:]
        res += word2[index:]
        return res
 

