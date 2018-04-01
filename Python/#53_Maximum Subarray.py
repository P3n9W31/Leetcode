class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        curSum = maxSum = nums[0]
        for num in nums[1:]:
            curSum = max(num, curSum + num)
            print('curSum: ' + str(curSum))
            maxSum = max(maxSum, curSum)
            print('maxSum: ' + str(maxSum))

        return maxSum