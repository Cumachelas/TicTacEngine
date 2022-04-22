# TicTacEngine v1.2.2 (22.04.2022) - made by @Cumachelas
# Use the described below methonds and objects to quickly build your own TicTacToe games!

from array import *
import random
import copy
class CellOccupiedError(Exception):
    pass
class BoardOverflowError(Exception):
    pass
class InvalidCellError(Exception):
    pass
class Mark:
    
    # Defined players, designed for expansion
    X = "X"
    O = "O"
    EMPTY = " "
    
    # Constructor for 'Mark'
    def __init__(self, active=X, scoreX:int=0, scoreO:int=0, starting=None) -> None:
        self.active:str = active
        self.scoreX:int = scoreX
        self.scoreO:int = scoreO
        self.starting:Mark = active

    # Iterates to the next player, either from active or from one passed
    def nextPlayer(self, active_player=None):
        if active_player:
            self.active = copy.deepcopy(active_player)
            return self.active
        if self.active == Mark.X:
            self.active = Mark.O
        elif self.active == Mark.O:
            self.active = Mark.X
    
    # Iterates to the next starting player from the last starting player
    def nextStartingPlayer(self):
        if self.starting == Mark.X:
            self.active = self.starting = Mark.O
        elif self.starting == Mark.O:
            self.starting = self.starting = Mark.X
    
    # Returns winner based on current scores
    def getWinner(self):
        if self.scoreX > self.scoreO:
            return "X"
        elif self.scoreO > self.scoreX:
            return "O"
        elif self.scoreX == self.scoreO:
            return "Draw"
class Board:
    
    ONGOING = "ongoing"
    DRAW = "draw"
    WINX = "X"
    WINO = "O"
    
    # Intiating the array with loops to avoid the shallow loop
    emptyBoard = [[Mark.EMPTY for i in range(3)] for j in range(3)]
    last_move:list = None
    
    def __init__(self, state:list=emptyBoard, move_count:int=0) -> None:
        self.state = state
        self.move_count = move_count
    
    # Checks whether the given cell is occupied
    def isOccupied(self, cell:list):
        if self.state[cell[0]][cell[1]] != Mark.EMPTY:     
            return True
        else:
            return False
    
    # Checks state if the game - returns either the winner, "draw", or "ongoing"
    # Argument --terminal automatically raises the score for the game by 1
    def getCondition(self, mark_instance:Mark=None, args:str=""):
        
        # Check row integrity
        for r in range(3):
            if self.state[r][0] == self.state[r][1] == self.state[r][2] and self.state[r][2] != Mark.EMPTY:
                return self.state[r][0]
    
        # Check column integrity
        for c in range(3):
            if self.state[0][c] == self.state[1][c] == self.state[2][c] and self.state[2][c] != Mark.EMPTY:
                return self.state[0][c]
        
        # Check diagonal integrity
        if self.state[0][0] == self.state[1][1] == self.state[2][2] and self.state[2][2] != Mark.EMPTY:
            return self.state[0][0]
        elif self.state[0][2] == self.state[1][1] == self.state[2][0] and self.state[2][0] != Mark.EMPTY:
            return self.state[0][2]
        
        # Check for a draw/full board
        for row in self.state:
            if not any(Mark.EMPTY in row for row in self.state):
                return self.DRAW
        
        # If no conditions are met, the game is still ongoing
        return self.ONGOING
    
    # Writes safely to a cell, thows Exception if occupied
    def safeWrite(self, cell:list, player:Mark):
        global last_move
        if not 0 <= cell[0] <= 2 or not 0 <= cell[1] <= 2:
            raise InvalidCellError("safeWrite() input out of valid range")
        if self.isOccupied(cell):
            raise CellOccupiedError("safeWrite() cell already occupied")
        else:
            last_move = cell
            self.move_count += 1
            self.state[cell[0]][cell[1]] = copy.deepcopy(player)
    
    # Prints graphical state of the board to CLI
    def prettyprint(self):
        output = ""
        for row in range (3):
                output += f"{self.state[row][0]} | {self.state[row][1]} | {self.state[row][2]}\n---------\n"
        print(output.rstrip("\n-"))
    
    # Prints the board in array form to CLI
    def cprint(self):
        print(self.state)
    
    # Plays a random move for a given player
    def makeRandomMove(self, player:Mark):
        while True:
            try:
                self.safeWrite([random.randint(0,2), random.randint(0,2)], player)
            except CellOccupiedError: continue
            else: break
    
    # Fills the board with given number of random marks while considering the playability of the board
    def fillBoard(self, mark_instance:Mark, depth:int=random.randint(1,8)):
        if depth > 9:
            raise BoardOverflowError("fillBoard() depth too large")
        else:
            for i in range(depth):
                if self.getCondition() != self.ONGOING:
                    self.undoMove()
                    break
                else:
                    self.makeRandomMove(mark_instance.active)
                    Mark.nextPlayer(mark_instance)
    
    # Clears the board
    def clear(self):
        self.state = copy.deepcopy(self.emptyBoard)
            
    # Undoes the given, or if none passed, the last move
    def undoMove(self, given_move:list=[]):
        global last_move
        if not given_move:
            self.state[last_move[0]][last_move[1]] = Mark.EMPTY
        else:
            self.state[last_move[0]][last_move[1]] = copy.deepcopy(given_move)