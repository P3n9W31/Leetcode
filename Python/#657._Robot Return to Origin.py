class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        L_move = moves.count('L')
        R_move = moves.count('R')
        U_move = moves.count('U')
        D_move = moves.count('D')
        if L_move == R_move and U_move == D_move:
            return True
        return False