class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}
        for cs in s:
            count[cs] = count.get(cs, 0) + 1
        
        for ct in t:
            count[ct] = count.get(ct, 0) - 1

            if count[ct] < 0:
                return False

        return True  