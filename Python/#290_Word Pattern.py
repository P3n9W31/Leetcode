class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if len(pattern) != len(str.split(' ')):
            return False
        dic = {}
        for pat, word in zip(pattern,str.split(' ')):
            if pat not in dic.keys():
                dic[pat] = word
            elif word != dic[pat]:
                return False
            if len(dic.values()) != len(set(dic.values())):
                return False
        return True