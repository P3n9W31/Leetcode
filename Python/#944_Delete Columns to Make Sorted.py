class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        row_len = len(A)
        column_len = len(A[0])
        delete_column = []
        for column_index in range(column_len):
            column_cur = []
            for row_index in range(row_len):
                column_cur.append(A[row_index][column_index])
            if column_cur != sorted(column_cur):
                delete_column.append(column_index)
        return len(delete_column)

class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        return sum([sorted(item) != list(item) for item in zip(*A)])