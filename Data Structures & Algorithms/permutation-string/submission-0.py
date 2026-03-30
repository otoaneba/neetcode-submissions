class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False
        
        count1 = [0] * 26
        count2 = [0] * 26
        
        for c in s1:
            count1[ord(c) - ord('a')] += 1
        
        left = 0
        for right in range(m):
            count2[ord(s2[right]) - ord('a')] += 1
            
            # maintain window size = n
            if right - left + 1 > n:
                count2[ord(s2[left]) - ord('a')] -= 1
                left += 1
            
            if count1 == count2:
                return True
        
        return False
        "" 
