class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # edge cases:
        # empty array
        # array with only one value
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]

        # set prefix as first value, then iterate starting from the second element
        currLongestPrefix = strs[0]
        for i in range(1, len(strs)):
            for j in range(len(currLongestPrefix)):
                if j > len(strs[i])-1:
                    currLongestPrefix = currLongestPrefix[:len(strs[i])]
                    break
                if currLongestPrefix[j] != strs[i][j]:
                    currLongestPrefix = currLongestPrefix[:j]
                    break
        return currLongestPrefix

                