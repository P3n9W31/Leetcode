class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        buff = {}
        for index, item in enumerate(nums):
            if item in buff and index - buff[item] <= k:
                return True
            buff[item] = index
        return False
        