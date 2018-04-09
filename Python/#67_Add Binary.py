class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = a[::-1]
        b = b[::-1]
        if len(a)>len(b):
            b = b + '0'*(len(a) - len(b))
        else:
            a = a + '0'*(len(b) - len(a))
        ab_sum = []
        buff = 0
        for index in range(len(a)):
            if int(a[index]) + int(b[index]) == 2:
                if buff >= 1:
                    ab_sum.append('1')
                else:
                    ab_sum.append('0')
                    buff += 1
            elif int(a[index]) + int(b[index]) == 1:
                if buff >= 1:
                    ab_sum.append('0')
                else:
                    ab_sum.append('1')
            elif int(a[index]) + int(b[index]) == 0:
                if buff >= 1:
                    ab_sum.append('1')
                    buff -= 1
                else:
                    ab_sum.append('0')
        if buff != 0:
            ab_sum.append('1')
        ab_sum.reverse()
        return ''.join(ab_sum)