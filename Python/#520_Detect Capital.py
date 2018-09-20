class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word[0].islower():
            for alp in word[1:]:
                if alp.isupper():
                    return False
            return True
        
        if word[0].isupper():
            count = 0
            for alp in word:
                if alp.isupper():
                    count += 1
            if count == len(word) or count == 1:
                return True
            else:
                return False


class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.isupper() == True or word.islower() == True or word.istitle() == True:
            return True
        return False
        