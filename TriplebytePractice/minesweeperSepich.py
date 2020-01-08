import random
# Board Space object
class BoardSpace(object):
    def __init__(self):
        self.status = 0
        self.revealed = False


# Board object
class Board(object):
    def __init__(self, rows, cols, m_count):
        self.rows = rows
        self.cols = cols
        self.revealedCount = 0
        self.mines = m_count
        self.gameOver = False
        self.gameWon = False
        self.board = [[BoardSpace() for i in range(cols)] for j in range(rows)]
        count = 0
        while count < m_count:
            row = random.randint(0, rows - 1)
            col = random.randint(0, cols - 1)
            if self.board[row][col].status == -1:
                continue
            else:
                self.addMine(row, col)
                count += 1

    def __str__(self):
        # print row by row
        # first col is empty and always exists
        result = ''
        result += '   |'
        for r in range(self.rows + 1):
            if r > 0:
                result += ' ' + str(r-1) + ' |'
                for i in range(self.cols):
                    # r is row
                    # i is col
                    if self.board[r-1][i].revealed:
                        result += ' ' + str(self.board[r - 1][i].status) + ' |'
                    else:
                        result += '   |'
            else:    
                for i in range(self.cols):
                    result += ' ' + str(i) + ' |'
            result += '\n'
            for i in range(self.cols + 1):
                result += '----'
            result += '\n'
        return result

    def addMine(self, r, c):
        self.board[r][c].status = -1
        for row in range(r-1, r+2):
            for col in range(c-1, c+2):
                if row >= 0 and row < self.rows and col >= 0 and col < self.cols and self.board[row][col].status != -1:
                    self.board[row][col].status += 1
    
    def chooseSpace(self, r, c):
        # hit mine
        if self.board[r][c].status == -1:
            for row in range(self.rows):
                for col in range(self.cols):
                    self.board[row][col].revealed = True
            self.gameOver = True
            self.gameWon = False
            return
        self.board[r][c].revealed = True
        self.revealedCount += 1
        if self.rows * self.cols - self.revealedCount == self.mines:
            self.gameOver = True
            self.gameWon = True
        # if zero space go out
        if self.board[r][c].status == 0:
            for row in range(r-1, r+2):
                for col in range(c-1, c+2):
                    if row >= 0 and row < self.rows and col >= 0 and col < self.cols and self.board[row][col].revealed == False:
                        self.chooseSpace(row, col)

# esentailly main function
def playGame():
    # get board size
    rowCount = 1
    colCount = 1
    try:
        rowCount = int(input('Please enter number of rows: '))
        if rowCount <= 0:
            rowCount = int(input('Please enter number of rows: '))
        colCount = int(input('Please enter number of columns: '))
        if colCount <= 0:
            colCount = int(input('Please enter number of columns: '))
        mineCount = int(input('Please enter number of mines: '))
        if mineCount <= 0 or mineCount >= rowCount * colCount:
            mineCount = int(input('Please enter number of mines: '))
    except:
        print('Error reading input')
        return
    # initiate game state
    board = Board(rowCount, colCount, mineCount)
    print(board)
    while board.gameOver == False:
        r = -1
        if r < 0 or r >= rowCount:
            r = int(input('Pick a row: '))
        c = -1
        if c < 0 or c >= colCount:
            c = int(input('Pick a column: '))
        board.chooseSpace(r, c)
        if board.gameOver:
            break
        print(board)
        print('\n')
    
    print(board)
    if board.gameWon:
        print('Congratulations! You have won.')
    else:
        print('KABOOM. Good luck next time.')
    try:
        playAgain = int(input('Enter 1 to play again: '))
        if playAgain == 1:
            playGame()
    except:
        return


playGame()