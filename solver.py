from board import Board
from copy import deepcopy

EMPTY = 0
BOARD_DIMENSION = 9
BACKTRACKING = 0

class Solver:

    def __init__(self):
        ''' Creates a Solver object that can give a solution to a Sudoku board. '''
        self.solution = None
    
    def solve(self, sudoku_board: Board, algorithm = BACKTRACKING) -> Board:
        ''' Solves the Sudoku board given the algorithm. The default argument is
            the backtracking algorithm. Returns the solved Board object. '''
        if algorithm == BACKTRACKING:
            self.solution = self.backtracking(sudoku_board)

        return self.solution

    def backtracking(self, sudoku_board):
        ''' Solves the Sudoku Board using the backtracking algorithm. '''
        if sudoku_board.solved():
            return sudoku_board
        
        board_copy = deepcopy(sudoku_board)

        for i in range(BOARD_DIMENSION):
            for j in range(BOARD_DIMENSION):
                if board_copy.empty_cell(i, j):
                    for number in range(1, BOARD_DIMENSION + 2):
                        # Board has ran out of possible entries for that (row, column) -> Invalid Board
                        if number == BOARD_DIMENSION + 1:
                            return None
                        
                        if board_copy.valid_move(number, i, j):
                            board_copy.insert(number, i, j)
                            res = self.backtracking(board_copy)

                            if res == None:
                                board_copy.undo(number, i, j)
                            else:
                                return res
    
