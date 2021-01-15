import sys
from boards import board_states
import numpy as np

grid = board_states[1]
print(np.matrix(grid))

def possible(y, x, n):
	global grid
    # check row
	for i in range(0, 9):
		if grid[y][i] == n:
			return False
    # check column
	for i in range(0, 9):
		if grid[x][i] == n:
			return False
    
    # check square
	x0 = (x//3)*3
	y0 = (x//3)*3
	for i in range(0, 3):
		for j in range(0, 3):
			if grid[y0+i][x0+j] == n:
				return False
	return True

# def solve():
# 	global grid
# 	for y in range(9):
# 		for x in range(9):
# 			if grid[y][x] == 0:
# 				for n in range(1, 10):
# 					if possible(y, x, n):
# 						grid[y][x] = n
# 						solve()
# 						grid[y][x] = 0
# 				break
# 	print(np.matrix(grid))
# 	input("Next? ")

# solve()

game_board = board_states[1]

print(np.matrix(game_board))
print(game_board[0][2])
def count_empty_tiles(board):
	# how we will determine if the board is full, meaning the game should end
	count = 0
	for row in board:
		count = count + row.count(0)
	return count



def play_game(board):
	pass

# def main():
# 	pass
# 	# play_game(board_states[0])
# 	# print(np.matrix(board_states[0]))


# if __name__ == "__main__":
#     main()
