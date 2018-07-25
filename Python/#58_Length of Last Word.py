class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        count = 0
        length = 0
        tri = 0
        for word in s[::-1]:
            length += 1
            if word != ' ':
                tri = 1
            if tri == 0 and length == len(s):
                return 0
            
            if tri == 1:
                if length == len(s) and word != ' ':
                    count += 1
                if word == ' ' or length == len(s):
                    return count
                else:
                    count += 1