class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if 1 not in nums:
            return 0
        start = nums.index(1)
        end = start
        cur_count = 0
        max_count = 0
        for index in range(nums.index(1), len(nums)):
            if nums[index] == 1 and nums[index-1] == 1:
                end = index
            elif nums[index] == 1 and nums[index-1] == 0:
                start = index
                
            # if nums[index] == 0 or index == len(nums):
            cur_count = end - start + 1
            if cur_count > max_count:
                max_count = cur_count
        return max_count