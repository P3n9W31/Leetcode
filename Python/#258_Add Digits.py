class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if len(str(num)) == 1:
            return num
        while len(str(num)) != 1:
            ans = 0
            for i in str(num):
                ans += int(i)
            num = ans
        return ans