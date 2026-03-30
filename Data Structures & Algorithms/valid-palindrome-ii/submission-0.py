class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        h a n n a h a

        h a n n a x h

        trickiest thing about this is figuring out which character to skip when we're met with
        two characters that aren't equal. We have to check both. 

        h a n n a x h 
          l.      r

        in this situation, we analyze both left and right side, and if either is a palindrome, 
        then we can conclude that the string is a palindrome after deleting at most one character.
        So we check two strings:
          1. a n n a <- omit the left edge or s[l: r]
          2. n n a x <- omit the right edge or s[l+1:r+1]

        """
        l, r = 0, len(s) - 1
        while l < r:
          if s[l] != s[r]:
            # if r == len(s) - 1:
            #   return self.isPalindrome(s[l:r]) or self.isPalindrome(s[l+1:r+1])
            # else:
            return self.isPalindrome(s[l:r]) or self.isPalindrome(s[l+1:r+1])
          l += 1
          r -= 1
        return True

    def isPalindrome(self, s: str) -> bool:
      l, r = 0, len(s) - 1
      while l < r:
        if s[l] != s[r]:
          return False
        l += 1
        r -= 1
      return True
    
