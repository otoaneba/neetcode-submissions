class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        anagrams = {}
        freq = [0] * 26

        for each value in strs:
            freq = [0] * 26
            for each letter in value:
                populate freq
            freq = tuple(freq)
            if freq not in anagrams:
                put freq as key and inialize with [value]
            otherwise:
                append value into anagrams[freq]
        
        return List(anagrams.values())
        """
        anagrams = {}
        freq = [0] * 26

        for value in strs:
            freq = [0] * 26
            for c in value:
                index = ord(c) - ord('a')
                freq[index] += 1
            freq = tuple(freq)
            if freq not in anagrams:
                anagrams[freq] = [value]
            else:
                anagrams[freq].append(value)
        
        return list(anagrams.values())
