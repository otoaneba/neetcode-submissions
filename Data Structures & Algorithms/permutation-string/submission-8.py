class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        - we can use a sliding window technique that looks for window size s1 because 
          that's the exact size we need to create a permutation.
        - need the exact same number of characters within a specific window
            - map (not a set because we need a value, or count per character)
            - alphabet map with array
        - we can check freq of each character iteratively, which would take O(m) per window, 
          so a total of O(n * m). To improve that, we can have a match counter and a need,
          where a match counts total number of correct frequency we have within a window,
          and a need counts how many matches we need in order to make a permutation. 
            - need is the number of unique characters (each having its own freq)
            - match is the number of unique characters in the window (and its freq)
        - if the length of s2 is shorter than s1, we return False because we can't 
          create a permutation of s1 from a shorter string
        - we create the freqMap of s1 and the first mth characters of s2, where m is 
          the length of s1. need is length of s1 freq map.
        
        - for each character in s1's freqMap, we check against the first mth freqMap of
          s2. If they match, we increment have. 
        
        - run a for loop starting at len(s1) until len(s2)
            - if match == need return true
            - add s2[r] in s2 freqMap if not already and add 1
                - if s2[r] is now one less than s1[r] (s2[r] - 1), then we have surplus so decrement match
                - else if s2[r] == s1[r], increment match
            
            - remove or decrement s2[l] in s2 freqMap
                - if s2[l] is now one more than s1[l] (s2[l] + 1), then we had a match but now we dont' so decrement match
                - elseif s2[l] == s1[l], increment match
            

        """
        if len(s2) < len(s1):
            return False
        
        s1FreqMap = [0] * 26
        s2FreqMap = [0] * 26

        for i in range(len(s1)):
            s1FreqMap[ord(s1[i]) - ord('a')] += 1
            s2FreqMap[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if s1FreqMap[i] == s2FreqMap[i] and s1FreqMap[i] > 0:
                matches += 1
        
        need = 0
        for i in range(len(s1FreqMap)):
            if s1FreqMap[i] > 0:
                need += 1
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == need:
                print(s1FreqMap, s2FreqMap, need, matches, r)
                return True
            
            r_index = ord(s2[r]) - ord('a')
            s2FreqMap[r_index] += 1
            if s1FreqMap[r_index] > 0:
                if s1FreqMap[r_index] == s2FreqMap[r_index] - 1:
                    matches -= 1
                elif s1FreqMap[r_index] == s2FreqMap[r_index]:
                    matches += 1
            
            l_index = ord(s2[l]) - ord('a')
            s2FreqMap[l_index] -= 1
            if s1FreqMap[l_index] > 0:
                if s1FreqMap[l_index] == s2FreqMap[l_index] + 1:
                    matches -= 1
                elif s1FreqMap[l_index] == s2FreqMap[l_index]: 
                    matches += 1
            l += 1
        return matches == need



