import sys, pygame




# https://www.101computing.net/sudoku-generator-algorithm/
pygame.init()

# class Game:
valid = True
game_end = False
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

def checkDup(list):
	# checking valid rows, cols, squares on board
	seen = set()
	for x in list:
		if x in seen:
			return True
		seen.add(x)
	return False

def printBoard(board):
	# for i in board:
	# 	print(i
	print("-"*37)
	for i, row in enumerate(board):
		print(("|" + " {}   {}   {} |"*3).format(*[x if x != 0 else " " for x in row]))
		if i == 8:
			print("-"*37)
		elif i % 3 == 2:
			print("|" + "---+"*8 + "---|")
		else:
			print("|" + "   +"*8 + "   |")


		
def updateBoard(board, new_val, cords):
	# cords should be an x,y tuple
	board[cords[0]][cords[1]] = new_val

def validCol(col_num):
	# zero indexed
	col_vals = []
	for x in board:
		col.append(board[x][col_num])
	

	if not checkDup(col_vals):
		return True


def validSquare(square_key):
	# square_index is 1-9

	if not checkDup(squares_dict[square_key]):
		return True

	if not valid:
		print("Invalid board state")
	pass

def validRow(row):
	# valid = True
	if not checkDup(row):
		return True


def playGame(board):
	while not game_end:
		# printBoard(board)
		printBoard(board)
		# input("Input value to update, use form: [new value] [x coordinate] [y coordinate] \n")
		x = int(input("Enter x coordinate ((0,0) is top left): "))
		y = int(input("Enter y coordinate (0 indexed): "))
		new_val = int(input("Enter new value: "))
		print(board[x][y])
		print(board[y][x])
		if board[x][y] != 0:
			updateBoard(board, new_val, (x, y))
			printBoard(board)
			break
		else:
			print("Tile already filled")

		# get moves from sys
		# updateBoard
		# do validity checks


def main():
	printBoard(board)
    # playGame(board)

if __name__ == "__main__":
    main()
