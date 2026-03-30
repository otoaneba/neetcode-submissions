class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # we cannot make a permuation inside a shorter string 
        if len(s1) > len(s2):
            return False
        
        freq = Counter(s1)
        required = len(freq) # amount of unique characters
        matches = 0
        l = 0

        for r in range(len(s2)):
            rc = s2[r]
            if rc in freq:
                freq[rc] -= 1
                if freq[rc] == 0:
                    matches += 1
            
            if r - l + 1 > len(s1):
                lc = s2[l]
                if lc in freq:
                    if freq[lc] == 0:
                        matches -= 1
                    freq[lc] += 1
                l += 1
            if matches == required:
                return True
        return False
                