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


def newBoard(y,x):
	board = []
	for yy in range(int(y)):
		line = ['◻' for i in range(int(x))]
		board.append(line)
	return board

"""
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
"""

# ◼ ◻

def count(c, v):
	ret = 0
	for e in c:
		if e == v:
			ret += 1
	return ret

def printBoard(board):
	result = ""
	rown = 0
	r = ""
	for y, row in enumerate(board):
		if rown in range(0,10):
			result+=str(rown)+"  "
			rown+=1
		else:
			result+=str(rown)+" "
			rown+=1
		for x, c in enumerate(row):
			if c=="ы":
				result+="\033[42m◻\033[0m"
				continue
			if c=="а":
				result+="\033[42m◻\033[0m"
				continue
			if c==".":
				result += "◻"
				continue
			n = get_neighbours(board, y, x)
			co = count(n, ".")
			if co > 0 and "◼" in n:
				result += str(co)
			else:
				result += c
		result += '\n'
	result += "   "
	for i in range(len(board[0])):
		result+=str(i%10)
	result += "\n   "
	for i in range(len(board[0])):
		d = i//10
		if d == 0:
			result += " "
			continue
		result+=str(d)
	return result

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
	print(step, mod, board[step[0]][step[1]])
	if mod == 0: #digging mode
		if board[step[0]][step[1]] not in".":
			board[step[0]][step[1]]= "◼"
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
	if mod == 1: #marking mode
		if board[step[0]][step[1]]==".":
			board[step[0]][step[1]]= "ы"
		else:
			board[step[0]][step[1]]= "а"
	if mod == 2: #unmarking mode
		if board[step[0]][step[1]]=="ы":
			board[step[0]][step[1]]="."
		else:
			board[step[0]][step[1]]= "◻"

def boom(step,board):
	if board[step[0]][step[1]]==".":
		return True

def main():
	#print("Размер поля: ", end="")
	y,x = 20, 40
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
	while True:
		print(printBoard(board))
		print("Режим: ", end="")
		mod = int(input())
		print("Ход: ", end="")
		step = list(map(int, input().split()))
		turn(board,step,mod)
		if mod == 0:
			if boom(step,board):
				break
	'''
	'''
if __name__ == "__main__":
    main()