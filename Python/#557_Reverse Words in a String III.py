class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = s.split(' ')
        for index in range(len(word_list)):
            word_list[index] = word_list[index][::-1]
        return ' '.join(word_list)