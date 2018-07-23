class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == [] :
            return ''
        min_len = 1000
        for word in strs:
            if len(word) < min_len:
                min_len = len(word)
                min_word = word
        if min_len == 0:
            return ''
        prefix = strs[0][0]
        index = 0
        while index <= min_len:
            for i in range(len(strs)):
                if strs[i][0:index+1] != prefix:
                    if len(prefix) == 1:
                        prefix = ''
                    else:
                        prefix = prefix[:-1]
                    index = 1000
                    break
                elif i == len(strs) - 1:
                    index += 1
                    if index < min_len:
                        prefix += strs[0][index]
                    else:
                        return min_word
        return prefix