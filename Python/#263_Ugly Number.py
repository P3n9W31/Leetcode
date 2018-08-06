class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        if num == 0:
            return False
        
        if num % 2 == 0:
            num_sub = num // 2
        elif num % 3 == 0:
            num_sub = num // 3
        elif num % 5 == 0:
            num_sub = num // 5
        else:
            return False
        
        return self.isUgly(num_sub)