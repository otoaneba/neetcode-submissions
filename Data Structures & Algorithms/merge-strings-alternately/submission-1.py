class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # res = ""
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

        n, m = len(word1), len(word2)
        res = []
        i = j = 0
        while i < n or j < m:
            if i < n:
                res.append(word1[i])
            if j < m:
                res.append(word2[j])
            i += 1
            j += 1
        return "".join(res)

