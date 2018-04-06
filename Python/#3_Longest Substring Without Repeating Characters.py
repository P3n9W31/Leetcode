class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        buff = {} 
        max_count = 0
        start = 0
        end = 0
        for index in range(len(s)):
            if s[index] in buff and start <= buff[s[index]]:
                start = buff[s[index]] + 1
                end = index

            else:
                end = index
                count = end - start +1
                if count > max_count:

                    max_count = count
            buff[s[index]] = index
        return max_count