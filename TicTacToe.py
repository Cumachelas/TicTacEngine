from TicTacEngine import Board
from TicTacEngine import Mark
from array import *

board = Board()
players = Mark(starting=Mark.O)

board.fillBoard(players)
board.prettyprint()
print(board.checkForWinner() + " " + str(board.move_count))