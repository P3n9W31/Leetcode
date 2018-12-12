class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) == 1:
            return True 
        state = A[-1] - A[0]
            
        if state > 0:
            for num_index in range(1,len(A)):
                if A[num_index] < A[num_index - 1]:
                    return False
        if state < 0:
            for num_index in range(1,len(A)):
                if A[num_index] > A[num_index - 1]:
                    return False
                
        if state == 0:
            for num_index in range(1,len(A)):
                if A[num_index] != A[num_index - 1]:
                    return False
        return True
    