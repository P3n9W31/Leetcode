class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if len(nums)%2 == 0:
            for num_index in range(0,len(nums),2):
                if nums[num_index] != nums[num_index + 1]:
                    return nums[num_index]
        else:
            for num_index in range(0,len(nums)-1,2):
                if nums[num_index] != nums[num_index + 1]:
                    return nums[num_index]
            return nums[len(nums)-1]