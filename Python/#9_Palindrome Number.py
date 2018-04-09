class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        ranger = 1
        while x / ranger >= 10:
            ranger *= 10

        while x:
            left = x // ranger
            right = x % 10
            if left != right:
                return False
            x = (x % ranger) // 10
            ranger /= 100

        return True

# Shorter Solution
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        ans = 0
        num = x
        while num > 0:
            # print(ans,num)
            ans = ans * 10 + num % 10
            num = num // 10
        return ans == x


# Using Extra Space
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return int(str(abs(x))[::-1]) == x