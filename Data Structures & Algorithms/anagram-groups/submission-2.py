class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            freq = [0] * 26
            for letter in word:
                index = ord('a') - ord(letter)
                freq[index] += 1
            freq = tuple(freq)
            if freq not in anagrams:
                anagrams[freq] = [word]
            else:
                anagrams[freq].append(word)
        
        return list(anagrams.values())