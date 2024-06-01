# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from random import randint
     
class Board:
    """
    Main board class. Defines board size (rows and columns),
    the player's name, the number of ships
    """
    def __init__(self, size, name, board, ships):
        self.size = size
        self.name = name
        self.board = []
        for x in range(size):
            row = []
            for x in range(size):
                row.append('-')
                self.board.append(row)
            self.ships = []    
            
    def position_ship(self, index_row, index_col):
        """
        Function to position ships on the player's board marked as 'S'
        """       
        self.board[index_row][index_col] = 'S'
        self.ships.append((index_row, index_col))
            
            
        
