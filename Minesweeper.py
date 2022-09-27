#Minesweeper
import random
import re

class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        self.board = self.make_new_board() # plant the bombs
        self.assign_values_to_board()
        
        self.dug = set() # if we dig at 0,0, then self.dug = {(0,0)}
    
    #generate a new board
    def make_new_board(self):
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1)
            row = loc // self.dim_size
            col = loc % self.dim_size

            if board[row][col] == '*':
                # this means there's a bomb there already so keep going
                continue
            board[row][col] = '*' # plant the bomb
            bombs_planted += 1

        return board
    
    def assign_values_to_board(self):
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)

    def get_num_neighboring_bombs(self, row, col):
        num_neighboring_bombs = 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if r == row and c == col: # original location
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1
        
        return num_neighboring_bombs

def dig(self, row, col):
    #dig at location
    # return True if successful dig, False if bomb dug
    self.dug.add((row, col))

    if self.board[row][col] == '*':
        return False
    elif self.board[row][col] > 0:
        return True
        
    for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
        for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
            if (r, c) in self.dug:
                continue #don't dig where you've already dug
            self.dig(r, c)
    return True

def __str__(self):
    visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
    for row in range(self.dim_size):
        for col in range(self.dim_size):
            if (row, col) in self.dug:
                visible_board[row][col] = str(self.board[row][col])
            else:
                visible_board[row][col] = ' '
    string_rep = ''

# play the game
def play(dim_size=10, num_bombs=10):
    # Step 1: create the board and plant the bombs
    board = Board(dim_size, num_bombs)
    # Step 2: show the user the board and ask for where they want to dig
    # Step 3a: if location is a bomb, show game over message
    # Step 3b: if location is not a bomb, dig recursively until each square is at least
    # next to a bomb
    # Step 4: repeat steps 2 and 3 until there are no more places to dig -> VICTORY!
    safe = True
    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        user_input = re.split(',(\\s)*', input("Where would you like to dig? Input as row,col: "))
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board.dim_size or col < 0 or col >= dim_size:
            print("Invalid location. Try again.")
            continue
        # if it's valid, we dig
        safe = board.dig(row, col)
        if not safe:
            # dug a bomb
            break
    if safe:
        print("Congratulations!!!! You didn't die!")
    else:
        print("Well, you died. Sucks to be you lol")
        board.dug = [(r,c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)

if __name__ == '__main__':
    play()