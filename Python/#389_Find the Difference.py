import string
class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_alpha = [s.count(word) for word in string.ascii_lowercase]
        t_alpha = [t.count(word) for word in string.ascii_lowercase]
        for index in range(26):
            if s_alpha[index] != t_alpha[index]:
                return string.ascii_lowercase[index]



class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        return list(collections.Counter(t)-collections.Counter(s))[0]