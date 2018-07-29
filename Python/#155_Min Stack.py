class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min = [float('inf')]
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.data.append(x)
        if x <= self.min[-1]:
            self.min.append(x)


    def pop(self):
        """
        :rtype: void
        """
        if self.data[-1] == self.min[-1]:
            self.min.pop(-1)
        self.data.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.data[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]
        # return min_num
        