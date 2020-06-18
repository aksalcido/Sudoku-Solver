EMPTY = 0
BOARD_DIMENSION = 9

class Board:

    def __init__(self, board: [list]):
        ''' Initializes a board object that represents the sudoku board. '''
        self.board = board

    def get_board(self) -> [list]:
        ''' Returns the 2d array of the board. '''
        return self.board
    
    def solved(self):
        ''' Checks if the board is solved, in this implementation, it means there are
            no empty spaces on the board. Since we manually check each insert individually. '''
        for i in range(len(self.board)):
            if EMPTY in self.board[i]:
                return False

        return True

    def insert(self, number, row, col):
        ''' Changes (row, col) of the board to equal the number argument. '''
        self.board[row][col] = number

    def undo(self, number, row, col):
        ''' Undos and removes the number from (row, col) of the board. '''
        self.board[row][col] = EMPTY
    
    def valid_move(self, number, row, col):
        ''' Checks if a number can be inserted into (row, col) of the board.
            Returns True if valid otherwise False. '''
        if self.board[row][col] != EMPTY:
            return False

        return self._check_axis(number, row, col) and self._check_3x3(number, row, col)

    def empty_cell(self, row, col):
        ''' Returns if (row, col) is an empty square on the board. '''
        return self.board[row][col] == EMPTY
    
    def _check_axis(self, number, row, col):
        ''' Checks if the number is on the same vertical or horizontal axis given
            the (row, col). '''
        for i in range(BOARD_DIMENSION):
            if self.board[row][i] == number or self.board[i][col] == number:
                return False
            
        return True
    
    def _check_3x3(self, number, row, col):
        ''' Checks if the number is already in the specific 3x3 grid. To find the 3x3
            grid we are checking, we use floor division to give an index of where the
            3x3 grid would be on the board. Multiplying the indices we find by 3 gives
            the start row and col of that grid. '''
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        
        for i in range(3):
            for j in range(3):
                if self.board[start_row + i][start_col + j] == number:
                    return False

        return True

    def display(self):
        ''' Prints the board out to the console. '''
        print(self)

    def __repr__(self):
        ''' Returns a str representation of the board which is used when displaying
            the board. '''
        board_str = ""
        board_str += '-' * 21 + '\n'

        for i in range(len(self.board)):
            board_str += '| '
            
            for j in range(len(self.board[i])):
                if self.board[i][j] == EMPTY:
                    board_str += '_ '
                else:
                    board_str += str(self.board[i][j]) + ' '
                
            board_str += '|\n'

        board_str += '-' * 21 + '\n'

        return board_str
