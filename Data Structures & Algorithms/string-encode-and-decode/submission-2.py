class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        Hello, World

        51#Hello15#Worldsssss

        String(len(strs[i])) + "#" + strs[i]
        
        use a pointer
        read the encoded string until the pointer is at the end of the encoded string
        first, read the string until reaching special delimiter, #
        take that string and convert to number
        while the pointer is less than the given number:
            build the string 
            once the pointer is at the end of the given number, add into string

        """
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

        

    def decode(self, s: str) -> List[str]:
        """
        create a pointer
        read the encoded string until the pointer is at the end of the encoded string
        first, read the string until reaching special delimiter, #
        take that string and convert to number
        while the pointer is less than the given number:
            build the string 
            once the pointer is at the end of the given number, add into string

        51#Hello15#Worldsssss
        ^

        5# -> 5
        strToAdd
            while pointer < pointer + 5:
                strToAdd += s[pointer]
                pointer += 1
        """

        """
        Tricks:
        use another pointer that reference index to make it easier not to lose track i.e. j = index
        use array splicing to get the string i.e. [index: j]
        """

        index = 0
        res = []
        print(s)
        while index < len(s):
            j = index
            while s[j] != "#":
                j += 1
            print(s[index:j])
            length = int(s[index:j])
            index = j+1
            j = index + length
            res.append(s[index:j])
            index = j
        return res
