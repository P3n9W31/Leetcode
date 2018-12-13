class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        A_sorted = []
        for num_index in range(len(A)):
            if A[num_index] % 2 == 0:
                A_sorted.insert(0, A[num_index])
            else:
                A_sorted.append(A[num_index])
        return A_sorted
    