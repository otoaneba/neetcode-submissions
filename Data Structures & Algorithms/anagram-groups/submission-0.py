class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord('a')] += 1
            
            count = tuple(count)

            if count in anagrams:
                anagrams[count].append(word)
            else:
                anagrams[count] = [word]

        return list(anagrams.values())

