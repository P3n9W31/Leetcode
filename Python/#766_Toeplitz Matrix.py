class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        height, length = len(matrix), len(matrix[0])
        for index_1 in range(1,height):
            for index_2 in range(1,length):
                if matrix[index_1][index_2] !=matrix[index_1-1][index_2-1]:
                    return False
        return True