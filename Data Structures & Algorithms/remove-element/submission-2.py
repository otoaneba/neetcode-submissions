class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        I can create an empty array, and add each element from the nums list
        other than the unwanted val, and return the list. But that would require a
        new list.

         v  
        [1, 1, 2, 3, 4]
               ^ 
        scanner1 -> find a value that is the val, and stop 
        scanner2 -> find a value that is NOT the val and swap values 

         v  
        [2, 1, 1, 3, 4]  
               ^
        swap the values,
        then move the scanners by one

            v  
        [2, 3, 1, 1, 4] 
                  ^

               v  
        [2, 3, 4, 1, 1] 
                     ^

         v
        [1, 2, 3, 4] scanner1 -> stop when the val is found
         ^           scanner2 -> keep moving until the value is !val

         v
        [2, 1, 3, 4] condition met, swap, increment both 
            ^  

            v
        [2, 3, 1, 4] condiion met, swap, increment both
               ^
               v
        [2, 3, 1, 4]
                  ^ 

                  v
        [1, 2, 4, 1]
               ^     

        write and read scanner
        counter (count for how many swaps to substract from the nums length)

        for read in range(len(nums)):
            if value at read is NOT val AND value at write IS value
                swap values
                count += 1
                increment write (implicitly increment read)
        return length of nums - count

        """
        write = 0
        for read in range(len(nums)):
            if nums[read] != val and nums[write] == val:
                nums[write], nums[read] = nums[read], nums[write]
                write += 1
            elif nums[write] != val:
                write += 1 
        return write

       
