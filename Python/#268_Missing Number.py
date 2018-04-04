class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        begin = 0
        end = len(nums)-1
        nums.sort()
        if nums[-1] == len(nums)-1:
            return nums[-1]+1
        if nums[0] != 0:
            return 0
        
        while True:
            mid = (begin + end)//2
            if nums[mid] == mid:
                begin = mid
            else:
                end = mid
            if end - begin == 1:
                return nums[begin] + 1