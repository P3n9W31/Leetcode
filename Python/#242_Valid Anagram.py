class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        s_set = set(s)
        return [s.count(i) for i in s_set] == [t.count(i) for i in s_set]