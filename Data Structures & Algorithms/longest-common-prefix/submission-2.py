class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # empty array
        # array with only one value
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]

        currLongestPrefix = strs[0]
        for i in range(1, len(strs)):
            for j in range(len(currLongestPrefix)):
                if j > len(strs[i])-1:
                    currLongestPrefix = strs[i]
                    break
                if currLongestPrefix[j] != strs[i][j]:
                    currLongestPrefix = currLongestPrefix[:j]
                    break
        return currLongestPrefix

                