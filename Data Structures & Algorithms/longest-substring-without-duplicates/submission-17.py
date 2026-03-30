class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        given a string s, return the length of longest substring without duplicate characters. 

        substring is a contiguous string with no duplicate characters.

        "zxyzxyz" -> 3
        "xxxx" -> 1

        can I use python? Can i use built-in libraries?
        what are we trying to optimize? time? can I use extra memory if necessary?
        will the string every be empty?
        Is it case sensitive? Meaning, does a == A ?
        Do we count special characters or numbers?
        will the string s always have an answer?


        """
        
        result = 0
        for i in range(len(s)):
            freqMap = set() 
            currMaxLength = 0
            for j in range(i, len(s)):
                if s[j] in freqMap:
                    result = max(currMaxLength, result) # result = 1
                    break
                else:
                    freqMap.add(s[j])
                    currMaxLength += 1
                    result = max(currMaxLength, result) 
        return result