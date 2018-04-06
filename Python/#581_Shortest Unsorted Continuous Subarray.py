class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = 0
        nums_sorted = nums[:]
        nums_sorted.sort()
        tra = 0
        if len(nums) == 1 or nums == nums_sorted:
            return 0
        for index in range(len(nums)):
            if nums[index] != nums_sorted[index]:
                end = index
                if tra == 0:
                    start = index
                    tra = 1
        return end-start+1