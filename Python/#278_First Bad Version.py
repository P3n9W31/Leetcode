# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        pre = 1
        las = n
        while pre <= las:
            mid = (las + pre)//2
            if isBadVersion(mid):
                if isBadVersion(mid-1) is False:
                    return mid
                las = mid
            else:
                pre = mid + 1