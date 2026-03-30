class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        writeIndex = 0

        for observerIndex, currValue in enumerate(nums):
            if currValue != val:
                nums[writeIndex] = currValue
                count += 1
                writeIndex += 1
        print(count)
        return count
            


        