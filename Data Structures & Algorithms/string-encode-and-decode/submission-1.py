class Solution:

    def encode(self, strs: List[str]) -> str:
        # for each string, take the length
        # append the length with a delimiter, &
        # return the string
        res = ""
        for s in strs:    
            res += str(len(s)) + "&" + s
        
        print(res)
        return res
        
    def decode(self, s: str) -> List[str]:
        res = []

        currIndex = 0

        while currIndex < len(s):
            j = currIndex
            while s[j] != "&":
                j += 1
            length = int(s[currIndex:j])
            currIndex = j + 1
            j = currIndex + length
            res.append(s[currIndex:j])
            currIndex = j
         
        return res



