# -*- coding: utf-8 -*-

from pronouncing import phones_for_word, stresses
from math import sqrt


# noinspection PyPep8Naming
def PoemSync(input_file: str, output_file: str, tau: int) -> float:
	"""

	Compute the sync of a poem.

	:param input_file: Where to read the poem from
	:param output_file: Where to output the stresses' matrix
	:param tau: Value to calculate the sync with
	:return: The even of all syncs (rounded to the 6th decimal digit)
	"""

	# Open the file and read all the lines, removing blank ones
	# Also, remove every character which isn't a letter
	with open(input_file, "r", encoding="utf-8") as input_stream:
		lines = tuple(filter(lambda string: len(string) > 1, map(edit_illegal_chars, input_stream)))

	# Transmute the list of lines into a matrix of stresses,
	# where each row is a line from the poem
	matrix = tuple(flat(map(stresses_for, line.split())) for line in lines)

	# Compute the sync value for every 2-rows combination
	syncs = tuple(compute_sync(row1, row2, tau) for i, row1 in enumerate(matrix[:-1]) for row2 in matrix[i + 1:])

	# Print the matrix to the specified file
	output_matrix(output_file, matrix)

	# Return the even of syncs, rounded to the 6th decimal digit
	return round(sum(syncs) / len(syncs) / 2, 6)


def compute_sync(row1: list, row2: list, tau: int) -> float:
	root = sum(row1) * sum(row2)
	return (c(row1, row2, tau) + c(row2, row1, tau)) / sqrt(root) if root else root


def output_matrix(file_path: str, matrix: tuple) -> None:
	"""

	Literally print the matrix on a file.

	:param file_path: The output file's path
	:param matrix: The matrix(Iterable[Iterable[Any]])
	:return: None
	"""

	# Print row and fill the blank spots in the matrix with 0's
	max_len = max(map(len, matrix))
	with open(file_path, "w", newline="\n", encoding="utf-8") as output_stream:
		for line in matrix:
			print("".join(map(str, line)) + "0" * (max_len - len(line)), file=output_stream, end="\n")
	return


def edit_illegal_chars(string: str) -> str:
	"""

	Remove illegal characters from the string.
	Changes apostrophes and dashes into spaces,
	removes other special characters.

	:param string: The input string
	:return: The edited string
	"""
	return "".join(char if char.isalpha() else " " for char in string)


def stresses_for(word: str) -> list:
	"""

	Computes how many stresses the word has.
	If it isn't known, returns many 0's as half the length of the word.
	Adds a 0 to the end, for convenience.

	:param word: Word to analyze
	:return: A list with the stresses
	"""
	phonetic = phones_for_word(word)
	return map(int, stresses(phonetic[0]).translate({50: "0"}) + "0") if phonetic else [0] * (len(word) // 2 + 1)


def flat(arr: map) -> list:
	"""

	A convenience function, used to flatmap.
	Man, I sure do miss java.

	:param arr: The array to flatten
	:return: The flattened array
	"""

	flattened = []

	for item in arr:
		flattened.extend(item)

	return flattened


def c(row1: list, row2: list, tau: int) -> int:
	"""

	Function c, used to compute the sync between two lines.

	:param row1: First line stresses
	:param row2: Second line stresses
	:param tau: Tau parameter
	:return: The function's value
	"""

	counter = 0

	for i, value in enumerate(row1):
		if value:
			if 1 in row2[max(0, i - tau):i + 1]:
				counter += 1

	return counter
