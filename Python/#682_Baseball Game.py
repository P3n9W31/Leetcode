
class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        for i in ops:
            if i == '+':
                stack.append(stack[-1] + stack[-2])
            elif i == 'C':
                stack.pop()
            elif i == 'D':
                stack.append(2 * stack[-1])
            else:
                stack.append(int(i))
        return sum(stack)


class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        work = [0]*len(ops)
        scord = [0]*len(ops)
        for op_index in range(len(ops)):
            if ops[op_index].isdigit() or ops[op_index].startswith('-'):
                scord[op_index] = int(ops[op_index])
                work[op_index] = 1
            if ops[op_index] == '+':  
                bias = 0
                num1 = 0
                num2 = 0
                while op_index - bias > 0:
                    bias += 1
                    if num1 == 0:
                        if work[op_index - bias] == 1:
                            num1 = int(scord[op_index - bias])
                    else:
                        if work[op_index - bias] == 1:
                            num2 = int(scord[op_index - bias])
                            
                    if num2 != 0:
                        scord[op_index] = num1 + num2
                        work[op_index] = 1
                        break
            if ops[op_index] == 'D':
                bias = 0
                num1 = 0
                while op_index - bias > 0:
                    bias += 1
                    if num1 == 0:
                        if work[op_index - bias] == 1:
                            num1 = int(scord[op_index - bias])
                    if num1 != 0:
                        scord[op_index] = num1 * 2
                        work[op_index] = 1
                        break
            if ops[op_index] == 'C':
                bias = 0
                num1 = 0
                while op_index - bias > 0:
                    bias += 1
                    if num1 == 0:
                        if work[op_index - bias] == 1:
                            num1 = int(scord[op_index - bias])
                    if num1 != 0:
                            scord[op_index] = num1 * (-1)
                            work[op_index - bias +1] = 0
                            work[op_index - bias] = 0
                            break
            
        return sum(scord)
        