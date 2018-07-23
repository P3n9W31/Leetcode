class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '':
            return True
        pair = {')':'(',']':'[','}':'{'}
        stack = []
        for sym in s:
            stack.append(sym)
            if sym in [')','}',']'] and len(stack) == 1:
                return False
            if sym in [')','}',']'] and stack[-2] == pair[sym]:
                stack.pop()
                stack.pop()
        if stack == []:
            return True
        return False