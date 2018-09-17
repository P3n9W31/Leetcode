class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return num^((2 ** len(str(bin(num))[2:])) - 1)
        