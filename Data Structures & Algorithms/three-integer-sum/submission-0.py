class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        we're given a list of integers, and I need to return all possible elements
        such that nums[i] + nums[j] + nums[k] = 0, and indices i,j,k must be disctinct.
        The outout should not have duplicates, and we can return them in any order.

        Input: nums = [-1,0,1,2,-1,-4]

        Output: [[-1,-1,2],[-1,0,1]]

        because  -1 + (-1) + 2 = 0, and -1 + 0 + 1 = 0

        can I assume I can use python and any build in libraries if needed?
        will the given array ever be empty?
        will each element in the array be valid?
        will the array fit into memory?
        what are we optimizing for? 
        if optimizing for time, can I use extra memory?
        will the array be sorted?
        can I sort the array?

        There's a similar pattern where I could use two pointers to solve this,
        and I want to try and see if this works.

        In order for that to work, the array would need to be sorted because 
        for each iteration I need to decided which pointer to move. 



        let's see if that works with target being 0. 

        [-1,0,1,2,-1,-4] 
        [-4, -1, -1, 0, 1, 2]
          l                r
          l              r
      l = -4 -> -4
      r =  2 ->  1
currSum = -2 -> -3

        [-4, -1, -1, 0, 1, 2]
          i.  j            k -> 1
                  j.       k -> 1
                     j.    k -> 2 
                        j  k -> 3
          j   i            k -> -2
                  j        k -> 1 ** [-1, -1, 2]
                  i
          j.               k -> -2
              j.           k -> 1 [-1, -1, 2]    

        i = -4 
        j and k such that -i = j+k because i = -(j + k)

        logic
        result = []
        i = 0
        j = 1
        k = len(nums)-1

        """
        nums.sort()
        result = []

       
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums)-1

            while j < k:
                print(i,j,k, ": ",nums[i], nums[j], nums[k])
                if nums[j] + nums[k] < -1 * nums[i]:
                    j += 1
                elif nums[j] + nums[k] > -1 * nums[i]:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
        


        return result
                