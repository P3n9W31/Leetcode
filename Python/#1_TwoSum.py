class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        rtype = []
        rest = []
        rest.extend(nums)
        counter = 0
        for index, a in enumerate(nums):
            counter = counter + 1       
            rest.pop(0)
            if target-a in rest:
                rtype.extend([index, rest.index(target-a)+counter])
        return rtype