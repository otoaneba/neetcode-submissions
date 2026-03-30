class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        window = set() # we need a set to analyze EVERY ELEMENT WITHIN THE WINDOW 
        l = 0 # we need a way to track the leftmost window edge
        for r in range(len(nums)): # we use a in range loop so that we can implicitly move the right pointer at every iteration
            if r - l > k: # we first check if window size is bigger than k because any analysis before this would mean checking values larger than k. If so, shrink from the left =
                window.remove(nums[l]) # remove the value at left edge
                l += 1 # increment the left 
            if nums[r] in window: # now check again if the current value at right edge, a new number, is in the window already. return true if so.
                return True
            window.add(nums[r]) # since the new value is NOT in the current window, add it to the window and move on.
        return False
                
            
