import sys, pygame




pygame.init()

# class Game:
valid = True
valid_entry = [1, 2, 3, 4, 5, 6, 7, 8, 9]


board = [
	[3, 0, 6, 5, 0, 8, 4, 0, 0],
	[5, 2, 0, 0, 0, 0, 0, 0, 0],
	[0, 8, 7, 0, 0, 0, 0, 3, 1],
	[0, 0, 3, 0, 1, 0, 0, 8, 0],
	[9, 0, 0, 8, 6, 3, 0, 0, 5],
	[0, 5, 0, 0, 9, 0, 6, 0, 0],
	[1, 3, 0, 0, 0, 0, 2, 5, 0],
	[0, 0, 0, 0, 0, 0, 0, 7, 4],
	[0, 0, 5, 2, 0, 6, 3, 0, 0]
]


squares_dict = {
	1: [board[0][0], board[0][1], board[0][2], board[1][0], board[1][1], board[1][2], board[2][0], board[2][1], board[2][2]],
	2: [board[0][3], board[0][4], board[0][5], board[1][3], board[1][4], board[1][5], board[2][3], board[2][4], board[2][5]],
	3: [board[0][6], board[0][7], board[0][8], board[1][6], board[1][7], board[1][8], board[2][6], board[2][7], board[2][8]],
	4: [board[3][0], board[3][1], board[3][2], board[4][0], board[4][1], board[4][2], board[5][0], board[5][1], board[5][2]],
	5: [board[3][3], board[3][4], board[3][5], board[4][3], board[4][4], board[4][5], board[5][3], board[5][4], board[5][5]],
	6: [board[3][6], board[3][7], board[3][8], board[4][6], board[4][7], board[4][8], board[5][6], board[5][7], board[5][8]],
	7: [board[6][0], board[6][1], board[6][2], board[7][0], board[7][1], board[7][2], board[8][0], board[8][1], board[8][2]],
	8: [board[6][3], board[6][4], board[6][5], board[7][3], board[7][4], board[7][5], board[8][3], board[8][4], board[8][5]],
	9: [board[6][6], board[6][7], board[6][8], board[7][6], board[7][7], board[7][8], board[8][6], board[8][7], board[8][8]],
}

def check_dup(list):
	# checking valid rows, cols, squares on board
	seen = set()
	for x in list:
		if x in seen and x != 0:
			return True
		seen.add(x)
	return False


def print_board(board):
	print("-"*37)
	for i, row in enumerate(board):
		print(("|" + " {}   {}   {} |"*3).format(*[x if x != 0 else 0 for x in row]))
		if i == 8:
			print("-"*37)
		elif i % 3 == 2:
			print("|" + "---+"*8 + "---|")
		else:
			print("|" + "   +"*8 + "   |")


		
def update_board(board, new_val, cords):
	# cords should be an x,y tuple
	board[cords[0]][cords[1]] = new_val
	return board

def valid_row(row):
	# valid = True
	if not check_dup(row):
		return True
	else:
		return False



def valid_col(col_num, board):
	# zero indexed
	col_vals = []
	for rows in board:
		col_vals.append(rows[col_num])
	print(col_vals)
	

	if not check_dup(col_vals):
		return True


def valid_square(square_key):
	# square_index is 1-9
	if not check_dup(squares_dict[square_key]):
		return True
	else:
		return False


def get_square_index(x, y):
	if x <= 2 and y <= 2:
		return 1
	elif y <= 2 and x >= 3 and x <= 5:
		return 2
	elif y <= 2 and x >= 6:
		return 3
	elif x <= 2 and y >= 3 and y <= 5:
		return 4
	elif x >= 3 and x <= 5 and y >= 3 and y <= 5:
		return 5
	elif x >= 6 and y >= 3 and y <= 5:
		return 6
	elif x <= 2 and y >= 6:
		return 7
	elif x>= 3 and x <= 5 and y >= 6:
		return 8
	else:
		return 9

# print(get_square_index(1, 1)) # 1
# print(get_square_index(3, 0)) # 2
# print(get_square_index(8, 8)) # 9
# print(get_square_index(6, 2)) # 3 
# print(get_square_index(4, 5)) # 5
# print(get_square_index(1, 5)) # 4
# print(get_square_index(7, 3)) # 6
# print(get_square_index(1, 7)) # 7


def count_empty_tiles(board):
	# how we will determine if the board is full, meaning the game should end
	count = 0
	for row in board:
		count = count + row.count(0)
	return count


def erase_tile(board):
	# need a means of changing a tile back to 0 if needed
	pass


def play_game(board):
	game_end = False
	remaining_zeros = count_empty_tiles(board)
	while not game_end:
		print_board(board)
		x = int(input("Enter x coordinate (left to right, (0,0) is top left): "))
		y = int(input("Enter y coordinate (up and down, 0 indexed): "))
		new_val = int(input("Enter new value: "))
		print(board[y][x])
		# print(board[y][x])
		square_index = get_square_index(x, y)
		print('Index: ' + str(square_index))
		if board[y][x] == 0:
			remaining_zeros = remaining_zeros - 1
			board = update_board(board, new_val, (y, x))
			print_board(board)
			break
		else:
			print("Tile already filled or invalid move in current board state")
		if remaining_zeros == 0:
			game_end = True

		# updateBoard
		# do validity checks
		# need a means of changing a tile back to 0 if needed


def main():
    play_game(board)
    # pass

if __name__ == "__main__":
    main()
