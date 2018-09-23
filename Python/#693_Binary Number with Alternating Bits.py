class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        b_bin = str(bin(n))[2:]
        start = b_bin[0]
        for alp in b_bin[::2]:
            if alp != start:
                return False
            
        for alp in b_bin[1::2]:
            if alp != str(int(start)^1):
                return False
        return True