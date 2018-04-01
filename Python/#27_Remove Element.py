class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        for index in range(len(nums)):
            if nums[index] != val:
                nums[count] = nums[index]
                count = count +1
        return count
        