from solver import Solver
from board import Board
from example_boards import ExampleBoards

GUI = True

if GUI:
    import tkinter as tk
    from view import View

def main():
    sudoku_solver = Solver()
    examples = ExampleBoards()
    
    if not GUI:
        sudoku_board = Board(examples.board_one())

        print("Sudoku Board to Solve: ")
        sudoku_board.display()
        
        solution = sudoku_solver.solve(sudoku_board)
    
        try:
            assert solution.get_board() == examples.solution_one()
        except AssertionError:
            print("Sudoku Board could not be solved")
        else:
            print("Solved Sudoku Board: ")
            solution.display()

    else:
        View(sudoku_solver, examples, tk.Tk()).run()
            
if __name__ == '__main__':
    main()
    
