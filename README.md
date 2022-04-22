# TicTacEngine
A simple, logical game engine module for all TicTacToe-based games. Primarily contains tools to manage boards, compute state and build AI players. TicTacDraw is a module coming soon to assist in drawing TicTacToe boards with common Python GUI libraries. Apart from that, TicTacEngine provides a solid framework for implementing MiniMax-based AI players, with ready-to-use methods coming soon.

### TicTac3Engine
Fully integrated platform to build 2-player, one 3x3 board games with. Contains all imaginable methonds for managing the boards, players and moves. Scroll down for a Quick Start guide.

### TicTac9Engine
A fully integrated UTTT (Ultimate TicTacTie) engine -> coming soon

# Quick Start with TicTac3Engine

**1. Put the module TicTac3Engine.py in your working directory and import it:**
  ```
  from TicTac3Engine import *
  ```
**2. Now, create an instance of the board and one of the player manager** (pass it the Mark you want to start the game with):
  ```
  board1 = Board()
  players = Mark(active=Mark.X)
  ```
**3. Let the players make random moves until the game is finished, print each one to the line** (either a win or a draw):
  ```
  while True:
  
    board.prettyprint()
    board.makeRandomMove(players.active) # players.active returns the next-to-move player
    board.nextPlayer()                   # iterates to the next player
    
    if board.getCondition != board.ONGOING: # checks whether the game has reached a terminal state...
      break
      
  print(board.getCondition)                 # ...and returns the result when it does
  ```
 4. Have fun and check out **TicTac3Engine.py** itself and the **SimpleTicTacToe.py** example to see all the methods!
      _(better docs are coming in the future)_
      
# Example of a 2-player game (SimpleTicTacToe.py)

```
from TicTac3Engine import *

# Create instance of the player manager and the playing board
players = Mark(active=Mark.X)
board = Board()

print("\nTicTacToe CLI - made with TicTacEngine v1.2.2")
print("Input the moves in format: [row from the top, 0-2],[column from right, 0-2]\n")
print(f"The player {players.active} is starting")

# Session Loop -> multiple games and total score
while True:
    
    # Clear the board
    board.clear()

    # Game Loop -> one game until terminal state
    while True:
        
        print("\n")
        board.prettyprint()
        
        # Input Loop -> until a valid move is put in
        while True:
            
            # Take user input in form (row,column) and convert it to list of integers
            move = input(f"Place an {players.active}: ").split(",")
            move = [int(i) for i in move]
            
            # Use the safeWrite() method to confirm move is legal, otherwise continue in the Input Loop
            try:
                board.safeWrite(move, players.active)
            except CellOccupiedError:
                print("Cell already taken!")
            else: break

        # Fetch the condition of the game, and break the game loop if terminal state is reached
        condition = board.getCondition(players)
        if condition == "O":
            players.scoreO += 1
            print("\nO wins")
            break
        elif condition == "X":
            players.scoreX += 1
            print("\nX wins")
            break
        elif condition == "draw":
            print("\nDraw")
            break
        
        # Iterate to the next player for the next move if no terminal state is reached yet
        elif condition == "ongoing":
            players.nextPlayer()
            continue
        
    # Print the score at the end of each round
    print(f"Score:\n{players.scoreX} (X) - {players.scoreO} (O)\n")
    
    # Ask if user wants another round, and breaks the Session Loop if not
    if input("Continue to next round? (y/n): ") == "y":
        pass
    else: break
    
    # Swap who starts the next round
    players.nextStartingPlayer()
```
      
