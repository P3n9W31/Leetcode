import string
class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(ransomNote) > len(magazine):
            return False
        if set(magazine) | set(ransomNote) != set(magazine):
            return False
        randsomNote_alpha = [ransomNote.count(word) for word in string.ascii_lowercase]
        magezine_alpha = [magazine.count(word) for word in string.ascii_lowercase]
        for word_index in range(26):
            if randsomNote_alpha[word_index] > magezine_alpha[word_index]:
                return False
        return True