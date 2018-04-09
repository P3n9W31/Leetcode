class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        alp = {'I':1, 'X': 10, 'C': 100, 'M': 1000, 'V': 5, 'L': 50,'D': 500}
        if len(s) == 1:
            return alp[s[0]]
        int_s = alp[s[0]]
        for index in range(1, len(s)):
            if alp[s[index-1]] >= alp[s[index]]:
                int_s += alp[s[index]]
            else:
                int_s += alp[s[index]] - 2*alp[s[index-1]]
        return int_s