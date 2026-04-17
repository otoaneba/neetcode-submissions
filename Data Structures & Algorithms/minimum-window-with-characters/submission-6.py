class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        create a character map array
        create a "need" and "have" vars where need is the number of character and its freq in t, and have is the current window in s
        create tCounter and sCounter together - count the freq of each character for t, and do the same for s for the length of t because that's the shortest window required to 
        for all characters in t, check if the freq matches the tCounter with sCounter. If so, increment need by 1
        create l and r pointer where l is 0 and r is len(t) - 1
        check if t is empty -> return ""
        create a res = ""
        create a length of current res
        
        start a loop until r reaches he length of s
          check if current window already has all the necessary characters -> return s[l:r+1]

          while have != need
            move the right pointer
          
          while the left pointer is not pointing to a character in t:
            move the left pointer
          
        """

        t_counter = Counter(t)
        window = {}
        have, need = 0, len(t_counter)
        res, res_len = [-1, -1], float("inf")
        l = 0

        for r in range(len(s)):
          window[s[r]] = window.get(s[r], 0) + 1

          if s[r] in t_counter and window[s[r]] == t_counter[s[r]]:
            have += 1
          
          while have == need: # explain why (why not have != need?)
            # shift left
            if r - l + 1 < res_len:
              res = [l,r]
              res_len = len(s[l:r+1])
            window[s[l]] -= 1
            if s[l] in t_counter and window[s[l]] < t_counter[s[l]]:
              have -= 1
            l += 1
        return s[res[0]: res[1]+1]