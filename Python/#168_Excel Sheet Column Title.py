class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        alp = [chr(i) for i in range(65,91)]
        excel = ''
        while n != 0:
            excel += alp[n%26-1]
            n = (n-1) //26
        excel = excel[::-1]
        return excel

class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        n_26 = []
        alp = [chr(i) for i in range(65,91)]
        excel = ''
        while n != 0:
            n_26.append(n%26)
            n = (n-1) //26
        for item in n_26[::-1]:
            excel += alp[item-1]
        return excel

class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        r = ''
        while(n>0):
            n -= 1
            r = chr(n%26+65) + r
            n //= 26
        return r