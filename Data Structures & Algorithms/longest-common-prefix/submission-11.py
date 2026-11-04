class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):
            j = 0
            while j < len(prefix) and j < len(strs[i]) and strs[i][j] == prefix[j]:
        
                j += 1
            prefix = prefix[0: j]
        return prefix