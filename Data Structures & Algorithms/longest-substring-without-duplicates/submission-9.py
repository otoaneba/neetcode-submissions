class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        given a string, s, find the longest length substring without duplicate characters.
        A substring is a contiguous sequence of characters within a string.

        Input: s = "zxyzxyz"
        Output: 3

        Input: s = "xxxx"
        output: 1

        Will the string ever be empty? If so, should we return 0?
        Are we optimizing for time? Can I use extra memory if so?
        Will the string fit into memory?
        Is this case sensitive?
        what type of characters will we analyze?
        does empty space count?

        zxyzyxz -> output is 3 because zxy is the longest substring within x without repeating
        any characters.


        input: s = "abcdef"
        output = 6

        input: s = "xxyyzz" 
        output = 2 (xx, yy, zz)

        {z, x, y }
        
            z x y z x y z 
            i 
              i
                i 
                  i
                    i
                      i 
                        i  
maxLength = 1>2>3>3>3>3>3
        """
        # if s == "":
        #     return 0
        
        # elif len(s) == 1:
        #     return 1

        # substringDict = {}
        # currMaxSubstring = ""
        # maxLength = 0
        # for char in s:
        #     if char not in substringDict:
        #         currMaxSubstring += char
        #         substringDict[char] = 1
        #         maxLength += 1
        #         substringDict[currMaxSubstring] = maxLength
        #     else:
        #         substringDict[currMaxSubstring] = maxLength
        #         currMaxSubstring = char
        #         maxLength = 1
        # print(substringDict, maxLength)
        # result = 0
        # for value in substringDict.values():
        #     if value > result:
        #         result = value
        # return result

        l = 0
        maxLength = 0
        seen = set()
        
        for char in range(len(s)):
            while s[char] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[char])
            maxLength = max(maxLength, char - l + 1)
        return maxLength

