class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = n
        cur_num_len = 1
        if n < 9:
            return n
        while n > 0:
            if cur_num_len == 1:
                tol_len = 9
            else:
                tol_len = ((10 ** cur_num_len) - 10 ** (cur_num_len-1)) * cur_num_len
            if count - tol_len > 0:
                    count -= tol_len
                    cur_num_len += 1
            else:
                low = 0
                high = (10 ** cur_num_len) - 10 ** (cur_num_len-1)
                mid = (low + high) // 2
                while low < high:
                    if count - mid * cur_num_len > 0 and count - (mid+1) * cur_num_len <= 0:
                        break
                    mid = (low + high) // 2
                    if count - mid * cur_num_len <= 0:
                        high = mid
                    else:
                        low = mid + 1
                break
        return int(str(10 ** (cur_num_len-1) + mid)[count - mid * cur_num_len - 1])