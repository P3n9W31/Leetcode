class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        buff = []
        r = []
        for index_1 in range(numRows):
            if index_1 == 0:
                r.append([1])
            elif index_1 == 1:
                r.append([1,1])
            else:
                for index_2 in range(index_1+1):
                    if index_2 == 0 or index_2 == index_1:
                        buff.append(1)
                    else:
                        buff.append(r[index_1-1][index_2] + r[index_1-1][index_2-1])
                r.append(buff)
                buff = []
        return r