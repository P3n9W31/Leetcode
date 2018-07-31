class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        bin_n = str(bin(n))[2:]
        for i in bin_n:
            if i == '1':
                count += 1
        return count