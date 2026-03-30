class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # for each character, check all possible substring within the string

        # for every substring, count the number of character frequency

        # calculate if the current length of substring has x amount of repeated characters
        # such that (current length of substring) - x <= k. Because if the remaining
        # number of characters that do not appear most frequent in the substring is 
        # more than the target, we cannot have repeated characters with the length of 
        # at least the current substring.

        # x a a a x a 
        # k = 2
        # if the substring we're looking at is x a a a x, the character we want to replace
        # is x because we have a limited number of switches (k), and so we need to minimize
        # the number of switches possible to create a repeated sequence. To do that, we 
        # must figure out the most frequent character in a substring, and check if the
        # !most-frequent characters count is less than k, and if so, we can make a substring
        # with all the same characters. 

        result = 0
        for i in range(len(s)):
          count, maxF= {}, 0
          
          for j in range(i, len(s)):
            count[s[j]] = count.get(s[j], 0) + 1

            maxF = max(maxF, count[s[j]])

            if (j - i + 1) - maxF <= k:
              result = max(result, j - i + 1)

        return result