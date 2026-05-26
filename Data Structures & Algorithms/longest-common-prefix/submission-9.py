class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        1. A prefix is anything that starts from the beginning.
        2. Since we're trying to find the longest common prefix, we have to look at all the strings in the array, and find the common prefix between each one of them.
        3. Given the first example, all strings start with a "ba", but since each one of them have unique third character, the response would be "ba"
        
        """

        prefix = strs[0]
        for i in range(1, len(strs)):
            index = 0
            while index < len(prefix) and index < len(strs[i]):
                if prefix[index] != strs[i][index]:
                    break
                index += 1
            prefix = prefix[0:index]
        return prefix