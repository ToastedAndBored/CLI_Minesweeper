from random import randint
from time import sleep

def newBoard(y,x):
	board = []
	for yy in range(int(y)):
		line = ['◻' for i in range(int(x))]
		board.append(line)
	return board
# ◼ ◻
	pass

def printBoard(board):
	result = ""
	for row in board:
		for c in row:
			result +=c
			if c=="☠":
				result+="◻"
		result += '\n'
	return result

def neigbours(board, y, x):
	ret = []
	for yy in [-1, 0, 1]:
		for xx in [-1, 0, 1]:
			if yy == 0 and xx == 0:
				continue
			if abs(xx-x)<=1 and abs(yy-y)<=1:
			#if yy < 0 or xx < 0 or yy >= len(board) or xx >= len(board[0]):
				#continue
				try:
					ret.append(board[yy][xx])
				except:
					pass
	return ret

def firstTurn(board,step,bombs):
	board[step[0]][step[1]]="◼"
	palnted = 0
	while palnted < bombs:
		y, x = randint(0, len(board)-1), randint(0, len(board[0])-1)
		if board[y][x] in ",◼":
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
				n = neigbours(board, y, x)
				if (board[y][x] == "◻") and ("." not in n):# and ("◼" in n):
					opened = True
					board[y][x] = "◼"
					break

def turn(board,step,mod):
	pass

def boom(step,board):
	if board[step[0]][step[1]]==".":
		return True

def main():
	print("Размер поля: ", end="")
	y,x = 20, 40
	#y,x = list(map(int, input().split(" ")))
	print("Количество бомб: ", end="")
	bombs = 40
	#bombs = int(input())
	board = newBoard(y,x)
	#print(printBoard(board))
	#print("Первый ход: ", end="")
	step = [19, 0]
	#step = list(map(int, input().split(" ")))
	firstTurn(board,step,bombs)
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