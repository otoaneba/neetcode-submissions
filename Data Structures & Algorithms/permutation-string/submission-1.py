class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        return true if s2 contains a permutation of s1. Otherwise, return false. Both strings
        contain only lowercase English letters.

        will either strings every be empty?
        will either strings have valid length or fit into memory?
        can I sort the string?
        what are we aiming to optimize? if time, can I use extra memory?
        can I use built-in library if needed?
        will either parameters ever be null or undefined?

        s1 = "abc", s2 = "lecabee"
        output: true 
        cab is a permutation of "abc"

        Input: s1 = "abc", s2 = "lecaabee"
        Output: false
        no permutation of "abc" in s2 

        Input: s1 = "a" s2 = "aaaa"
        Output: true

        s1 = "aab" s2 = "bbbbabb" 
        output: false

        solution 1:
        sort both s1 and s2, check for substring that match s1 in s2 
        mLogm + nLogn to sort, then n * m to look for the 


        we can use a sliding window pattern because this technique is great for keeping track of
        specific subarray and the values inside it, but i think the tricky part about this is
        that we need to constantly keep track of what's inside the window AND the characters 
        inside s1.. so we may need to have two maps.. we can't do sets because we need to count 
        for duplicate letters

        goal: abc 
        l = 0
        need = {a: 1, b: 1, c: 1}
        have = {}
        required = 0 //must much length of s1 because we need to match the count of every letter in s1 to create permutation 
        
        v   v   v   v   v
        l   e   c   a   a   e   e
         
        l  
            l
                l
                l
have = {}
            {} 
                {c}
                    {c, a}
                        {c, a, b}

        right moves every iteration
        if current letter is in need, AND "have"[current value] is not satisfied, add this to have
            if the current letter value in "have" equal to the current letter value in "need"? 
                add 1 to required
        if current letter is not in need, move the left one

        check if need == have 
        
        """
        count1 = Counter(s1)

        need = len(count1)
        # I thought that the length of need had to be the total number of characters, but 
        # all we need are the total number of unique characters.. why? if we're tracking 
        # total number of characters, we have to add the value for each character to get 
        # the current number. 

        # This method is still sort of brute force, but using hash map to iterate every substring
        # we build per ith character. So for every ith iteration, we create a NEW MAP.

        for i in range(len(s2)):
            count2, have = {}, 0
            for j in range(i, len(s2)):
                count2[s2[j]] = count2.get(s2[j], 0) + 1
                if count2[s2[j]] > count1.get(s2[j], 0):
                    break # we've exceeded the amount of letter we need 
                if count2[s2[j]] == count1.get(s2[j], 0):
                    have += 1
                if have == need:
                    return True
        return False
                

