class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # scan each row
        for i in range(len(board)):
            seenRow = set()
            for j in range(len(board)):
                if board[i][j] == '.':
                    continue
                if board[i][j] not in seenRow:
                    seenRow.add(board[i][j])
                else:
                    return False
    
        for i in range(len(board)):
            seenCol = set()
            for j in range(len(board)):
                if board[j][i] == '.':
                    continue
                if board[j][i] not in seenCol:
                    seenCol.add(board[j][i])
                else:
                    return False
    #    i = 0, 1, 2.  i = 3, 4, 5.  i = 7, 8, 9    len(0, 3) len(3, 6) len(6, 9)
    #    j = 0, 1, 2.  j = 0, 1, 2.  j = 0, 1, 2.       0  1.     1  2.     2  3

        for rowBase in (0, 3, 6):
            for colBase in (0, 3, 6):
                seenBox = set()
                for i in range(3):
                    for j in range(3):
                        if board[rowBase + i][colBase + j] == '.':
                            continue
                        if board[rowBase + i][colBase + j] not in seenBox:
                            seenBox.add(board[rowBase + i][colBase + j])
                        else:
                            return False
        return True
