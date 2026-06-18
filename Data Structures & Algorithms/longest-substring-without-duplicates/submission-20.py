class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        create a set
        create a r and left pointers, where r always moves one every iteration
        use a for loop with r as index
        while s[r] in set,
            remove the s[l] from set
            move the l pointer to the left
        res = max(res, r - l + 1)

        """
        seen = set()
        res = 0
        l = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            res = max(res, r - l + 1)
        return res