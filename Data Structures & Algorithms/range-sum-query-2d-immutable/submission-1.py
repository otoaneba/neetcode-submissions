class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.P = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        for r in range(ROWS):
            for c in range(COLS):
                self.P[r+1][c+1] = matrix[r][c] + self.P[r][c+1] + self.P[r+1][c] - self.P[r][c]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        P = self.P
        return (
            P[row2 + 1][col2 + 1]
            - P[row1][col2 + 1]         # strip the rows above
            - P[row2 + 1][col1]         # strip the columns to the left
            + P[row1][col1]             # add back the corner removed twice
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)