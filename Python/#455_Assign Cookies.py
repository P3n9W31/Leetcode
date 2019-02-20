class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        if s == [] or g == []:
            return 0
        children = reversed(sorted(g))
        cookies = sorted(s)
        cookies_len = len(cookies)
        count = 0
        
        for child in children:
            if child <= cookies[-1]:
                cookies.pop(-1)
                count += 1
            if len(cookies) == 0:
                return cookies_len
        
        return count
                