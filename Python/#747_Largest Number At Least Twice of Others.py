class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = max(nums)
        for item in nums:
            if item != 0 and item !=max_num and max_num//item <2:
                return-1
        return nums.index(max_num)