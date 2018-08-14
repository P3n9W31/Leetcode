class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        tra = 0

        for seat_index in range(len(seats)):
            if tra == 0:
                if seats[seat_index] == 1:
                    pre = aft = longest = seat_index
                    dis = 0
                    tra = 1
            else:
                if seats[seat_index] == 1:
                    aft = seat_index
                    dis = int((aft + pre)/2) - pre
                    pre = seat_index
                if seat_index == len(seats) - 1:
                    if seats[seat_index] == 0:
                        dis = len(seats) - 1 - aft
                if dis > longest:
                        longest = dis
                    
        return longest