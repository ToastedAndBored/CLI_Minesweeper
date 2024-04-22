from random import randint
from time import sleep
from neighbours import get_neighbours

DEFAULT = '''
◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻.◻◻
◻◻◻◻◻◻◻◻◻◻◻◻.◻◻◻◻◻◻◻.◻◻◻.◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻
◻◻◻◻◻◻◻◻◻◻◻.◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻
◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻
◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻.◻◻◻◻◻.◻◻◻.◻◻◻◻◻◻.◻◻◻◻◻
◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻.◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻
◻◻◻◻◻◻◻◻◻◻◻.◻◻◻◻..◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻
◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻.◻◻◻◻◻◻◻◻◻.◻◻◻◻◻◻◻◻◻◻◻◻◻
◻◻◻◻◻◻◻◻◻◻.◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻
◻◻.◻◻◻◻◻◻◻◻◻◻◻.◻◻◻◻◻.◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻.
◻◻◻◻.◻◻◻◻◻.◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻.◻◻◻◻◻◻◻
◻◻◻◻◻◻◻◻◻◻◻◻◻◻.◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻.
◻◻◻.◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻
◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻.◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻
◻◻◻◻◻◻◻.◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻
◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻.◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻.◻◻◻◻
◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻.◻◻◻◻◻.◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻
◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻.◻.◻◻◻◻◻◻.
◻◻◻◻◻◻◻◻◻◻.◻◻◻◻◻◻◻◻◻◻◻◻◻◻.◻◻.◻◻◻◻◻◻◻◻◻◻◻
◼◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻.◻◻◻.◻◻◻
'''
def remove_chars_whitelist(text):
	ret = ""
	for c in text:
		if c in ".◼◻\n":
			ret += c
	return ret

templates = ""
def newBoard(y,x,template=DEFAULT):
	if x ==0 and y == 0:
		cleaned_template = remove_chars_whitelist(template)
		cleaned_template += "\n"
		board = []
		line = []
		for cell in cleaned_template:
			if cell == "\n":
				if len(line) > 0:
					board.append(line)
				line = []
				continue
			line.append(cell)
		return board
	else:
		for yy in range(int(y)):
			line = ['◻' for i in range(int(x))]
			board.append(line)
		return board
# ◼ ◻
	pass

def count(c, v):
	ret = 0
	for e in c:
		if e == v:
			ret += 1
	return ret

def printBoard(board):
	result = ""
	for y, row in enumerate(board):
		for x, c in enumerate(row):
			if c==".":
				result += "◻"
			else:
				n = get_neighbours(board, y, x)
				co = count(n, ".")
				if co > 0 and "◼" in n:
					result += str(co)
				else:
					result += c
		result += '\n'
	return result

def nearBomb(board,y,x) -> bool:
	for yy in range(-1,1):
		for xx in range(-1,1):
			yy = yy + y
			xx = xx + x
		if board[yy][xx] == ".":
			try:
				return True
			except:
				pass
		else:
			try:
				return False
			except:
				pass

def neigboursIf(board, y, x):
	ret = []
	try:
		if board[y-1][x-1] in '.◼◻':
			try:
				ret.append(board[y-1][x-1])
			except:
				pass
		if board[y-1][x] in '.◼◻':
			try:
				ret.append(board[y-1][x])
			except:
				pass
		if board[y-1][x+1] in '.◼◻':
			try:
				ret.append(board[y-1][x+1])
			except:
				pass
		if board[y][x-1] in '.◼◻':
			try:
				ret.append(board[y][x-1])
			except:
				pass
		if board[y][x+1] in '.◼◻':
			try:
				ret.append(board[y][x+1])
			except:
				pass
		if board[y+1][x] in '.◼◻':
			try:
				ret.append(board[y+1][x])
			except:
				pass
		if board[y+1][x-1] in '.◼◻':
			try:
				ret.append(board[y+1][x-1])
			except:
				pass
		if board[y+1][x] in '.◼◻':
			try:
				ret.append(board[y+1][x])
			except:
				pass
	except:
		pass
	return ret

def neigbours(board, y, x):
	ret = []
	for yy in range(-1,1):
		for xx in range(-1,1):
			if yy == 0 and xx == 0:
				continue
			yy = yy + y
			xx = xx + x
			if (yy < 0 or xx < 0) or yy >= len(board) or xx >= len(board[0]):
				continue
			try:
				ret.append(board[yy][xx])
			except:
				pass
	return ret

"""
def firstTurn(board,step,bombs):
	board[step[0]][step[1]]="◼"
	palnted = 0
	while palnted < bombs:
		y, x = randint(0, len(board)-1), randint(0, len(board[0])-1)
		if board[y][x] in ".◼":
			continue
		board[y][x] = "."
		palnted+=1
	print()
	#board[step[0]][step[1]]="◻"
	opened = True
	while opened:
		print(printBoard(board)+"\n")
		sleep(0.1)
		opened = False
		for y in range(len(board)):
			if opened:
				break
			for x in range(len(board[0])):
				n = get_neighbours(board,y,x)
				print(n)
				if (board[y][x] == "◻") and ("." not in n):# and ("◼" in n):
					opened = True
					board[y][x] = "◼"
					break
"""
def firstTurn(board,step,bombs):
	board[step[0]][step[1]]="◼"
	palnted = 0
	while palnted < bombs:
		y, x = randint(0, len(board)-1), randint(0, len(board[0])-1)
		if board[y][x] in ".◼":
			continue
		board[y][x] = "."
		palnted+=1
	print()
	opened = True
	while opened:
		opened = False
		for y in range(len(board)):
			for x in range(len(board[0])):
				n = get_neighbours(board,y,x)
				if board[y][x] != "◻":
					continue
				if "◼" not in n:
					continue
				if "." in n:
					continue
				board[y][x] = "◼"
				opened = True
				#print(y, x)

def turn(board,step,mod):
	pass

def boom(step,board):
	if board[step[0]][step[1]]==".":
		return True

def main():
	#print("Размер поля: ", end="")
	y,x = 0, 0
	#y,x = list(map(int, input().split(" ")))
	#print("Количество бомб: ", end="")
	bombs = 40
	#bombs = int(input())
	board = newBoard(y,x)
	#print(board)
	#print(printBoard(board))
	#print("Первый ход: ", end="")
	step = [19, 0]
	#step = list(map(int, input().split(" ")))
	firstTurn(board,step,bombs)
	print(printBoard(board))
	return
	while True:
		print(printBoard(board))
		print("Режим: ", end="")
		mod = input()
		print("Ход: ", end="")
		step = input().split()
		turn(board,step,mod)
		if mod == 1:
			if boom(step,board):
				break
	'''
	'''
if __name__ == "__main__":
    main()