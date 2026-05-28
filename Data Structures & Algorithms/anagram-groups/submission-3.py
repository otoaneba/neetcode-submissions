class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        prefix = {}
        for word in strs:
            freq = [0] * 26
            for c in word:
                index = ord(c) - ord('a')
                freq[index] += 1
            
            freq = tuple(freq)
            if freq not in prefix:
                prefix[freq] = [word]
            else:
                prefix[freq].append(word)
        return list(prefix.values())