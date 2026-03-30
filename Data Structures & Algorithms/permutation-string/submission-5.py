class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count1, count2 = [0] * 26, [0] * 26
        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            matches += (1 if count1[i] == count2[i] else 0)
        
        l = 0
        for i in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            # expand the window by adding a new character to the right
            added = ord(s2[i]) - ord('a')
            count2[added] += 1
            if count1[added] == count2[added]:
                matches += 1
            elif count1[added] + 1 == count2[added]:
                matches -= 1
            
            # shrink the window by removing a character at the left
            removed = ord(s2[l]) - ord('a')
            count2[removed] -= 1
            if count1[removed] == count2[removed]:
                matches += 1
            elif count1[removed] - 1 == count2[removed]:
                matches -= 1
            l += 1

        
        return matches == 26
