class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            charMap = [0] * 26
            for c in s:
                index = ord(c) - ord('a')
                charMap[index] += 1
            charMap = tuple(charMap)
            if charMap in anagrams:
                anagrams[charMap].append(s)
            else:
                anagrams[charMap] = [s]
        return list(anagrams.values())