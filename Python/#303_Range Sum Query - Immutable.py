class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.data = nums
        self.sum = [0]*len(nums)
        if nums != []:
            
            self.sum[0] = self.data[0]

            for num_index in range(1, len(self.data)):
                self.sum[num_index] = self.sum[num_index-1] + self.data[num_index]
        
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sum[j] - self.sum[i] + self.data[i]