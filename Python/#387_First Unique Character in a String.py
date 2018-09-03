import string
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        alpha = list(string.ascii_lowercase)
        for word_index in range(len(s)):
            if s[word_index] in alpha:
                if s.count(s[word_index]) == 1:
                    return word_index
                else:
                    alpha.remove(s[word_index])
        return -1