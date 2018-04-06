        count = 0
        for index in range(len(bits)-2,-1,-1):
            if bits[index] == 1:
                count += 1
            else:
                break
        return count%2 == 0