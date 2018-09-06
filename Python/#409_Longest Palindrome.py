from collections import Counter
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        pal_len = 0
        has_one = 0
        counter = Counter(s)
        for word in dict(counter).values():
            if word % 2 == 0:
                pal_len += word
            else:
                if word != 1:
                    pal_len += word - 1
                has_one = 1
                
        if has_one == 1:
            return pal_len + 1
        return pal_len