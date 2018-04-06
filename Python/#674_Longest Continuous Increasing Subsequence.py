class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 1
        start = end = max_count = count = 0
        for index in range(1,len(nums)):
            if nums[index] <= nums[index-1]:
                count = end - start + 1
                start = index
            elif index == len(nums)-1:
                count = end - start + 2
                start = index
            if count > max_count:
                    max_count = count
            end = index
        return max_countpt