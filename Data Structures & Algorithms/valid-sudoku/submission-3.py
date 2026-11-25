class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
            nested for loop
            check each row
                if any duplicates
                    return false
            
            nested for loop
            check each column
                if any duplicates
                    return false
            
            nested for loops check 3 rows and 3 columns
            0,1,2   0,1,2

                    3,4,5

                    6,7,8
            
            
            3,4,5   0,1,2

                    3,4,5

                    6,7,8
            
            
            6,7,8   0,1,2

                    3,4,5

                    6,7,8
            
            


            00 01 02.  03 04 05  06 07 08  i == 0,   3,   6.       
            10 11 12.  13 14 15  16 17 18. j == 0    1.   2
            20 21 22   23 24 25  26 27 28  k == 

        """
        row_map = {}
        col_map = {}
        grid_map = {}

        row_map = {i: set() for i in range(len(board))}
        col_map = {j: set() for j in range(len(board[0]))}
        grid_map = {(i,j): set() for i in range(3) for j in range(3)}

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                if board[i][j] in row_map[i] or board[i][j] in col_map[j] or board[i][j] in grid_map[(i//3, j//3)]:
                    return False
                row_map[i].add(board[i][j])
                col_map[j].add(board[i][j])
                grid_map[(i//3,j//3)].add(board[i][j])
        return True
                