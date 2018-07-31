class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sys.setrecursionlimit(16)
        count = 0
        ans = 0
        for i in str(n):
            ans += int(i)**2
        if ans == 1:
            return True
        else:
            try:
                return self.isHappy(ans)
            except RecursionError:
                return False


class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        anss = []
        while True:
            ans = 0
            for i in str(n):
                ans += int(i)**2

            if ans == 1:
                return True
            else:
                if ans in anss:
                    return False
                anss.append(ans)
            n = ans