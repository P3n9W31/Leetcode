class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        column = len(A[0])
        row = len(A)
        A_T = [[0] * row for _ in range(column)]
        for i in range(column):
            for j in range(row):
                A_T[i][j] = A[j][i]
        return A_T