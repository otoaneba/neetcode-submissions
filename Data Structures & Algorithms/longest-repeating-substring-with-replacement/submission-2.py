class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        given a string s and an integer k, I can perform up to k times to change the characters
        in string s to any other characters in the alphabet. The string is made up of 
        capital letters in the English alphabet.

        return the longest substring which contains one character.

        language, goals.
        edge cases -> valid input, output, empty string, 
        extra memory allowed? use of built-int library allowed?

         "XYYX", k = 2
         4 because i can change the Ys to make all Xs (or change Xs to make all Ys)

         "AAABABB", k = 1'
         5 because i can change the first B to make AAAAABB, which has the longest contiguous
         character consisting of As with length 5.


         
        """
        """
        result = 0
        for i in range(len(s)):
          # if we initialize j with i+1, it becomes a bit too complex. If we start j from i, we
          # can simplify and move this logic below into the second loop
          # freqMap[s[i]] = freqMap.get([s[i]], 0) + 1 

          # mostFreq is a number. Not a character, so set it 0. The placement of this logic is correct.
          # mostFreq = s[i]
          mostFreq = 0

          # we're counting the freq each substring iteration, so we should initialize a map here
          counter = {}
          # count, maxF= {}, 0

          for j in range(i, len(s)):
            # add value and increment by 1 to counter if not in counter. If it's already in 
            # the counter, add 1. 
            counter[s[j]] = counter.get(s[j], 0) + 1 

            # most frequent is the maximum of the current character's value, and the saved mostFreq
            mostFreq = max(mostFreq, counter[s[j]]) 
            
            # if the current substring length - the mostFreq is still less than or equal to k,
            # the result is the max between the current substring length and last known longest result
            # we do this until j - i + 1 - mostFreq is less than or equal to k
            if j - i + 1 - mostFreq <= k:
              result = max(result, j - i + 1 )
          """
        maxF = 0
        res = 0
        counter = {}
        l = 0

        for r in range(len(s)):
          counter[s[r]] = counter.get(s[r], 0) + 1
          maxF = max(counter[s[r]], maxF)

          if r - l + 1 - maxF > k:
            counter[s[l]] -= 1
            l += 1
          res = max(res, r - l + 1)
        return res

