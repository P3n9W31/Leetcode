from functools import reduce
class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """

        if not nums:
            return []
        shaped = []
        height, length = len(nums), len(nums[0])
        if r * c != height * length:
            return nums
        nums[:] = reduce(lambda x,y:x+y, nums)
        for index_1 in range(r):
            shaped.append([int(nums[index_1*c + index_2]) for index_2 in range(c)])
        return shaped

class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r * c != len(nums) * len(nums[0]):
            return nums
        else:
            items = [y for x in nums for y in x]
            return [items[x*c : ((x+1)*c)] for x in range(r)]

