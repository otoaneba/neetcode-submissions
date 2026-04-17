class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
          1. can I use python and any built in libraries if necessary?
          2. what are we trying to optimize? time or space? can I use extra memory if optimizing for time?
          3. will the inputs s and t always be a valid string? no null or undefined?
          4. will t always be shorter than s?
          
          OUZODYXAZV      XYZ

          brute force can check every character and check every other character to see if all characters in t exists. I'll need a counter for t, and check 
          everytime we update if it's equal to t's counter. It's O(n^3) time becase we need to check every other character for each character, and for every
          iteration, we also need to check the map for the character count.

          we'll need
          1. tCounter 
          2. the current shortest substring
          3. the length of #2
          4. the current substring map 

          X:1, Y:1, Z:1
          O:2, U:1, Z:1, D:1, Y:1, X:1

          for every character i in s:
            add ch in sCounter
            for every other character j in s except ch:

              check if i exists in sCounter and add if not

              after adding, for each key in tCounter, check if they all match in sCounter
                if so, set shortest substring, its length and break

        """

        tCounter = Counter(t)
        res = ""
        resLength = float('inf')

        for i in range(len(s)):
          sCounter = {}
          
          for j in range(i, len(s)):
            sCounter[s[j]] = sCounter.get(s[j], 0) + 1

            is_valid = True
            for char in tCounter:
              if sCounter.get(char, 0) < tCounter[char]:
                is_valid = False
                break
            
            if is_valid:
              current_window = s[i:j+1]
              if len(current_window) < resLength:
                res = current_window
                resLength = len(res)
                break
        return res


