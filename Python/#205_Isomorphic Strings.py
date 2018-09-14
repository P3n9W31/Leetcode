from collections import Counter
class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        c_s = Counter(s)
        c_t = Counter(t)
        if sorted(list(dict(c_s).values())) != sorted(list(dict(c_t).values())):
            return False
        map_dict = {}
        for s_word,t_word in zip(s,t):
            if s_word not in map_dict.keys():
                map_dict[s_word] = t_word
            else:
                if t_word != map_dict[s_word]:
                    return False
        return True
            
        
        