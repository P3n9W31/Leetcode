class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        def bigger2K(s):
            front = s[:k]
            rest = s[k:]
            new_str = front[::-1] + rest
            front_str = new_str[:2*k]
            rest_str = new_str[2*k:]
            rest_len = len(rest_str)
            return front_str, rest_str, rest_len
            
        str_len = len(s)
        str_list = []
        rest_str = s
        if str_len < k:
            return s[::-1]
        elif str_len < 2*k and str_len >= k:
            return s[:k][::-1] + s[k:]
        
        while str_len >= 2*k:
            front_str, rest_str, rest_len = bigger2K(rest_str)
            str_len -= 2*k
            str_list.append(front_str)
            if rest_len < k:
                str_list.append(rest_str[::-1])
            elif rest_len < 2*k and rest_len >= k:
                str_list.append(rest_str[:k][::-1] + rest_str[k:])
                
        return ''.join(str_list)
        
        
        