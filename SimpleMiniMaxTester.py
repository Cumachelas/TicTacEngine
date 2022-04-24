from TicTac3Engine import *

board = Board()
players = Mark(active=Mark.X)

depth = 4
board.fillBoard(players, depth)

print(f"\nFilled board with {str(depth)} moves with player {players.starting} starting.\n")
board.prettyprint()
print(f"\nNow it's player {players.active}'s turn:")
print(f"Possible moves: {board.getMoves()}\n")

board.makeBestMove(mark_instance=players, args="--simpleminimax")

board.prettyprint()