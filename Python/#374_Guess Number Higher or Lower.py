class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if guess(n) == 0:
            return n
        low = 1
        high = n
        mid = (low + high)//2
        while guess(mid) != 0:            
            if guess(mid) == -1:
                high = mid
            elif guess(mid) == 1:
                low = mid
            mid = (low + high)//2
        
        return mid