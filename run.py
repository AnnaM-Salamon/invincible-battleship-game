# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from random import randint
     
class Board:
    """
    Main board class. Defines board size (rows and columns),
    the player's name, the number of ships
    """
    def __init__(self, size, name, board, num_ships, ships):
        self.size = size
        self.name = name
        self.num_ships = num_ships
        self.board = []
        for x in range(size):
            row = []
            for x in range(size):
                row.append('-')
                self.board.append(row)
            self.ships = []
def get_valid_input(self,prompt):
    while True:
        try:
            player_input = input(prompt)
            return int(player_input)
        except ValueError:
            print("Enter a valid number.")
                                      
                                      
def position_ship(self):
        """
        Function to position ships on the player's board marked as 'S'
        """       
       # print("Position your ships using row and column indexes startiong at 0: ")
    #    for ship_num in range(1, self.player_board.num_ships +1):
  #          while True:
 #          try:
 #              row = self.get_valid_input(f"Enter row number for a ship{ship_num}: ")
     #          col = self.get_valid_input(f"Enter column number for a ship{ship_num}: ")
     #           if
# #          self.player_board.can_position_ship(row, col)
#             self.player_board.position_ship(row, col)
# #             self.player_board.board[row][col] = 'S'