class Solution:
    def minWindow(self, s: str, t: str) -> str:
        "OUZODYXAZV"

        # "O"     -> "XYZ" 
        # "OU"    -> "XYZ"  
        # "OUZ"   -> "XYZ" 
        # "OUZO"  -> "XYZ"
        # "OUZOD" -> "XYZ"
        # "..."

        # "U"     -> "XYZ"
        # "UZ"    -> "XYZ"
        # "UZO"   -> "XYZ"
        # "UZOD"  -> "XYZ"
        # "UZODY" -> "XYZ"
        "..."


        # for each character in s, check if the substring that starts with i contains "XYZ"
        # If it does, save the length and the substring

        # we need set that includes all characters of t -> set(t)
        # we need the current longest length of the substring containing all char of t
        # we need the current longest substring that contains all char of t
        if len(t) > len(s):
            return ""

        target = Counter(t)
        shortest = ""

        for i in range(len(s)):
            window = Counter()

            for j in range(i, len(s)):
                window[s[j]] += 1

                valid = True
                for c in target:
                    if window[c] < target[c]:
                        valid = False
                        break

                if valid:
                    current = s[i:j+1]

                    if shortest == "" or len(current) < len(shortest):
                        shortest = current

                    break

        return shortest

    