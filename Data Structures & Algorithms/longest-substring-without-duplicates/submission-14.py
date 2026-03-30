class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        
        is this case sensitive?
        is it just alphabets? special characters? will spaces count as one character?
        will the string always be valid and non-empty?
        will this always have a solution?
        optimize for time? if so, extra memory allowed?

        Input: s = "zxyzxyz"
        Output: 3
        "xyz" zxy, yzx,

        longest = 1
        return 0 if s is empty
        return 1 if len(s) == 1

        have a left and right pointer for a sliding window
        have a set that saves all the values within the window

        "zxyzxyz"
        zx
        zxy
        zxyz -> shift left one 
         xyz
         xyzx -> shift left one again

        "zxyxxyz" 
        zx not the same? calculate longest by right - left + 1 and check max with longest, save elements at left and right into set, increment right += 1 (index: 2)
        zxy new element (y) inside set? calculate longest by right - left + 1 and check max with longest, save elements at left and right into set, increment right += 1 (index: 3)
        zxyx new element (x) inside set? , set left to last occured index of x and add 1. increment right, check max.
          yx
          yxx
            x
            xy
            xyz
        
        """
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        
        left = 0
        right = 0
        longest = 1
        freqMap = {}

        while right < len(s):
            if s[right] not in freqMap:
                    freqMap[s[right]] = right
                    # longest = max(longest, right - left + 1)
            else:
                
                print(freqMap[s[right]] )
                left = max(left, freqMap[s[right]] + 1)
                print("left is now: ", left)
                freqMap[s[right]] = right
            temp = right - left + 1
            longest = max(longest, temp)
            print(left, s[left],":", freqMap[s[left]], "| ", right, s[right], ":", freqMap[s[right]], longest)
            right += 1
        return longest

