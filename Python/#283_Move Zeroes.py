class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nums[:] = [item for item in nums if item != 0]
        nums.extend([0]*(n-len(nums)))