class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        o = ['a','e','i','o','u','A','E','I','O','U']
        o_word = []
        o_index = []
        s_list = list(s)
        for word_index in range(len(s)):
            if s[word_index] in o:
                o_word.append(s[word_index])
                o_index.append(word_index)
        o_index.reverse()
        
        for word_index_2 in range(len(o_index)):       
            s_list[o_index[word_index_2]] = o_word[word_index_2]
        
        return ''.join(s_list)