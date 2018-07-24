class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        p = 0
        while p <= len(haystack)-len(needle):
            if needle == haystack[p:p+len(needle)]:
                return p
            else:
                p += 1
        return -1