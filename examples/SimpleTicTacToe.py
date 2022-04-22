from TicTac3Engine import Board, Mark, CellOccupiedError

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