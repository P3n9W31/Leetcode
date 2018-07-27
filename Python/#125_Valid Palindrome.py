class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_s = ''
        s = s.lower()
        if s == '':
            return True
        
        for word in s:
            if word.isalnum():
                new_s += word
        
        pre = 0
        aft = len(new_s) - 1
        while pre < aft:
            if new_s[pre] == new_s[aft]:
                pre += 1
                aft -= 1
            else:
                return False
            
        return True