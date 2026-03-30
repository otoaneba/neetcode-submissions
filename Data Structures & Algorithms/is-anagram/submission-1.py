class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        set1 = {}
        set2 = {}
        for i in range(len(s)):
            if s[i] not in set1:
                set1[s[i]] = 1
            else:
                set1[s[i]] += 1
            if t[i] not in set2:
                set2[t[i]] = 1
            else:
                set2[t[i]] += 1
        return set1 == set2