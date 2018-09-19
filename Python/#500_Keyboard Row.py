class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = ['q','w','e','r','t','y','u','i','o','p']
        row2 = ['a','s','d','f','g','h','j','k','l']
        row3 = ['z','x','c','v','b','n','m']
        ans = []
        for word in words:
            is_ans = True
            if word[0].lower() in row1:
                word_row = row1 
            if word[0].lower() in row2:
                word_row = row2
            if word[0].lower() in row3:
                word_row = row3
                            
            for alp in list(set(word.lower())):
                if alp not in word_row:
                    is_ans = False
                    break
                    
            if is_ans:
                ans.append(word)
            
        return ans