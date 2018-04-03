class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        imp = []
        for index in range(len(numbers)):
            if numbers[index] not in imp:
                if target-numbers[index] in numbers[index+1:]:
                    return index+1,numbers[index+1:].index(target-numbers[index])+2+index
                else:
                    imp.append(numbers[index])