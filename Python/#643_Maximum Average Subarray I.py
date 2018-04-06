class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        return max([sum(nums[index:index+k]) for index in range(len(nums)-k+1)])/k


class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        max_sum = sum(nums[:k])
        cur_sum = max_sum
        for i in range(len(nums) - k):
            cur_sum = cur_sum - nums[i] + nums[i + k]
            if cur_sum > max_sum:
                max_sum = cur_sum
        return float(max_sum) / float(k)




