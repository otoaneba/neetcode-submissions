class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        "abc..z" -> a2c4z6 26(n) * n 
        [0] * 26 -> [1,... 1,... 1]
                     a.    c.    t

        { freqMap: ["act"...], }


        ["act","pots","tops","cat","stop","hat"]

     1. "act"
        [1,... 1,... 1]
         a.    c.    t

         {[1,... 1,... 1]: ["act"]}
        
     2. "pots"
        [1,... 1,... 1,...1]
         o.    p.    s.   t

        {
            [1,... 1,... 1]: ["act"], 
            [1,... 1,... 1,...1]: ["pots"]
        }

      3. "tops"
        [1,... 1,... 1,...1]
         o.    p.    s.   t 

        {
            [1,... 1,... 1]: ["act"], 
            [1,... 1,... 1,...1]: ["pots", "tops"]
        }

        init with anagrams = {}
        for each value str in strs
            create a freqMap for str
            if freqmap in anagrams:
                add current str
            else:
                initialize with array with current str
        
        return anagrams.values()
        """

        anagrams = {}
        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1
            freq = tuple(freq)
            if freq in anagrams:
                anagrams[freq].append(s)
            else:
                anagrams[freq] = [s]
        
        return list(anagrams.values())
