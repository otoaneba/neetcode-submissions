class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set()
        for num in nums:
            nums_set.add(num)
        
        start_sequence = []
        for num in nums_set:
            if num - 1 not in nums_set:
                start_sequence.append(num)
        
        longest_sequence = 0
        for start in start_sequence:
            current_sequence = 1
            while start + current_sequence in nums_set:
                current_sequence += 1
            longest_sequence = max(current_sequence, longest_sequence)
        
        return longest_sequence

        

