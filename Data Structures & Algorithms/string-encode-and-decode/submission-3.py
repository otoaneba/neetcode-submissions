class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        #10message
        10#message12#
        """
        res = ""
        for s in strs:
            length = str(len(s))
            res += length + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        """
        5#hello5#world
        res = []
        length = 0
        if pointer is at "#"
        left = 0
        while right < len(s)
            if right == "#":
                length = int(s[l:r])
                right += 1
                value = s[r:r+length]
                res.append(value)
                right += length
                left = right + length
            else:
                right += 1
        """
        res = []
        length = 0
        right = 0
        left = 0
        while right < len(s):
            if s[right] == "#":
                length = int(s[left:right])
                left = right + 1
                right = left + length
                value = s[left:right]
                res.append(value)
                left = right
            else:
                right += 1
        return res
