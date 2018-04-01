class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return [int(num) for num in str(int(''.join([str(i) for i in digits])) +1)]
