class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tol_sum = 0
        nums.sort()
        for index in range(len(nums)):
            if index%2 == 0:
                tol_sum = tol_sum + nums[index]
        return tol_sum


class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])