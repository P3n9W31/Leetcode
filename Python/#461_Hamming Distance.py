class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x_b = str(bin(x))[2:]
        y_b = str(bin(y))[2:]
        count = 0
        if len(x_b) <= len(y_b):
            x_b = '0' * (len(y_b) - len(x_b)) + x_b
        else:
            y_b = '0' * (len(x_b) - len(y_b)) + y_b
            
        for num_1, num_2 in zip(x_b, y_b):
            if num_1 != num_2:
                count += 1
        return count

class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return (bin(x^y)).count('1')
            
        
        