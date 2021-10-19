"""
File: boggle.py
Name: Jess
----------------------------------------
Implement a game of Boggle,
returning all valid words on a randomized game-board.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	First, load the dictionary into the words list
	Second, user creates the game-board with case insensitive
	Third, find words
	"""

	words_lst = read_dictionary([])
	game_board = user_input([])
	existed = []
	start = time.time()
	word_searcher(existed, words_lst, game_board)
	print(f'There are {len(existed)} words in total.')
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def word_searcher(existed, word_lst, board):
	"""
	This function finds all the words in the boggle game-board.

	:param existed: (lst) when found the word, it would append into this list
	:param word_lst: (lst) dictionary list
	:param board: (lst) game-board
	:return: This function doesn't return anything
	"""
	neighbor = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
	for y in range(len(board)):
		for x in range(len(board[y])):
			search_helper(existed, neighbor, word_lst, board, board[y][x], y, x, {(y, x)})


def search_helper(existed, neighbor, vocabs, game_board, cur,  y, x, taken):
	"""
	take in the current position (x,y ) on the board,
	and search all possible words starts with that char in the board.

	:param existed: (lst) saving the word that has been found already
	:param neighbor: (lst) the neighbor's (x,y) of current position
	:param vocabs: (lst) the dictionary words list
	:param game_board: (lst) the boggle game-board
	:param cur: (str) the character current steps on
	:param y: (int) cur's y position
	:param x: (int) cur's x position
	:param taken: (set) saving the cur that has been used
	"""
	# base case
	if cur in vocabs:
		if cur not in existed:
			existed.append(cur)
			print('Found', cur)

	# prefix
	if len(cur) == 2:
		if not has_prefix(cur[:2], vocabs):
			return

	# recursion
	for dx, dy in neighbor:
		(new_x, new_y) = (dx + x, dy + y)
		if in_board(game_board, new_y, new_x):
			if (new_y, new_x) not in taken:
				# choose
				taken.add((new_y, new_x))
				# explore
				search_helper(existed, neighbor, vocabs, game_board, cur+game_board[new_y][new_x], new_y, new_x, taken)
				# un-choose
				taken.remove((new_y, new_x))


def in_board(game_board, y, x):
	"""
	check the position is in board or out of board, when finding the neighbors.

	:param game_board: (lst) game-board
	:param y: neighbor's y position
	:param x: neighbor's x position
	:return: (bool)
	"""
	return 0 <= y < len(game_board) and 0 <= x < len(game_board[y])


def user_input(tbl):
	"""
	:param tbl: lst, saving the user's customized game-board
	:return: tbl
	"""
	first_row = input('1 row of letters: ')
	fir_r = ''
	check(first_row)
	for ch in first_row:
		if ch.isalpha():
			fir_r += ch.lower()
	tbl.append(fir_r)

	sec_row = input('2 row of letters: ')
	s_r = ''
	check(sec_row)
	for ch in sec_row:
		if ch.isalpha():
			s_r += ch.lower()
	tbl.append(s_r)

	third_row = input('3 row of letters: ')
	th_r = ''
	check(third_row)
	for ch in third_row:
		if ch.isalpha():
			th_r += ch.lower()
	tbl.append(th_r)

	fourth_row = input('4 row of letters: ')
	fou_r = ''
	check(fourth_row)
	for ch in fourth_row:
		if ch.isalpha():
			fou_r += ch.lower()
	tbl.append(fou_r)

	return tbl


def check(row):
	"""
	check whether there's illegal format, if Yes, exit the code
	:param row: the row of the game_board
	"""
	if len(row) == 7:
		for i in range(len(row)):
			if i % 2 == 0:
				if not row[i].isalpha():
					print('Illegal input')
					exit()
			else:
				if not row[i] == ' ':
					print('Illegal input')
					exit()
	else:
		print('Illegal input')
		exit()


def read_dictionary(lst):
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		for line in f:
			words_lst = line.split()
			for word in words_lst:
				if len(word) >= 4:
					lst.append(word)
	return lst


def has_prefix(sub_s, vocabs_list):
	"""
	:param vocabs_list: (lst) words in the dictionary
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""

	for word in vocabs_list:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
