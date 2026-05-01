class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        use 2sum approach after fixing first two indices. Skipping same values 
        ensures that we don't add duplicate quadruples.

        use a for loop from 0 to n
        i = 0 (if i > 0 and i the same as i-1, continue)
        j = i+1 (if j > i+1 and j the same as j-1, continue)
        left, right = j+1, n-1
        total = i + j + left + right
        if total == target
            add [i, j, left, right]
            left += 1
            right += 1
            while left is the same as left - 1
                left += 1
            while right is the same as right + 1
                right -= 1
        else
            left += 1
            right -= 1

        return the response at end

        """
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                l, r = j + 1, n - 1
                while l < r:
                    total = nums[i] + nums[j] + nums[l] + nums[r]
                    if total == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    elif total < target:
                        l += 1
                    else:
                        r -= 1
        return res


        