class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r = 0, len(s)-1
        while l < r:
          if s[l] != s[r]:
            # either left is palindrome or right is palindrome otherwise false
            return self.isPalindrome(s[l:r]) or self.isPalindrome(s[l+1:r+1])
          l += 1
          r -= 1
        return True
    
    def isPalindrome(self, s: str) -> bool:
      l,r = 0, len(s)-1
      while l < r:
        if s[l] != s[r]:
          return False
        l += 1
        r -= 1
      return True