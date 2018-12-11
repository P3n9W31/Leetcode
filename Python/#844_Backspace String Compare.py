import string
class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s_stack = []
        t_stack = []
        for alp in S:
            if alp in string.ascii_lowercase:
                s_stack.append(alp)
            if alp == '#':
                if len(s_stack) != 0:
                    s_stack.pop()
        for alp in T:
            if alp in string.ascii_lowercase:
                t_stack.append(alp)
            if alp == '#':
                if len(t_stack) != 0:
                    t_stack.pop()
        
        return True if s_stack == t_stack else False
                