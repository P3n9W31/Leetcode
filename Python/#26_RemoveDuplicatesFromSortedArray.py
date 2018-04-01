class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        count = 0
        for index in range(1,len(nums)):
            if nums[index] != nums[count]:
                count = count + 1
                nums[count] = nums[index]
        return count + 1