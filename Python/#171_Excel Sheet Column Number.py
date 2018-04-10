class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        ans = 0
        for item in s[::-1]:
            ans += ((ord(item))-65+1)*26**count
            count += 1
        return ans

class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        from functools import reduce
        return reduce(lambda x, y : x * 26 + y, [ord(c) - 64 for c in list(s)])

class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        num=0
        for i,x in enumerate(s):
            num+= (ord(x)-65+1) * 26 ** (n-i-1)
        return num