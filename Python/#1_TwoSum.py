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

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        new_nums = sorted(nums)
        front = 0
        end = len(new_nums) - 1
        solution = []
        while front < end:
            if new_nums[front] + new_nums[end] == target:
                solution.extend([new_nums[front], new_nums[end]])
                break
            elif new_nums[front] + new_nums[end] < target:
                front += 1
            else:
                end -= 1
        if solution[0] == solution[1]:
            return [nums.index(solution[0]), len(nums) - 1 - nums[::-1].index(solution[1])]
        return [nums.index(solution[0]), nums.index(solution[1])]