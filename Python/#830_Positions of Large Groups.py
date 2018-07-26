class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        start = 0
        end = 0
        count = 1
        i = 0
        big = []
        while i <= len(S)-2:
            if S[i+1] == S[i]:
                count += 1
            if S[i+1] != S[i] or i == len(S) - 2:
                end += count -1
                if count >= 3:
                    big.append([start, end])
                start = end + 1
                end = start
                count = 1
            i += 1
            
        return big