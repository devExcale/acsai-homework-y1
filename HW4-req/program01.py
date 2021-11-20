# -*- coding: utf-8 -*-

from pronouncing import phones_for_word, stresses
from math import sqrt


# noinspection PyPep8Naming
def PoemSync(input_file: str, output_file: str, tau: int) -> float:
	"""

	:param input_file:
	:param output_file:
	:param tau:
	:return:
	"""

	with open(input_file, "r", encoding="utf-8") as input_stream:
		rows = tuple(filter(None, map(normify_string, input_stream.readlines())))

	matrix = tuple(flat(map(stresses_for, line.split())) for line in rows)

	max_len = max(map(len, matrix))
	matrix = tuple(tuple(row + ([0] * (max_len - len(row)))) for row in matrix)

	syncs = []
	for row1 in matrix:
		for row2 in matrix:
			if row1 is row2:
				continue
			root = sum(row1) * sum(row2)
			syncs.append((c(row1, row2, tau) + c(row2, row1, tau)) / sqrt(root) / 2 if root else root)

	with open(output_file, "w", newline="\n", encoding="utf-8") as output_stream:
		for line in matrix:
			print("".join(map(str, line)), file=output_stream, end="\n")

	return round(sum(syncs) / len(syncs), 6)


def normify_string(string: str) -> str:
	return "".join(char if char.isalpha() else " " if char in " '-" else "" for char in string)


def stresses_for(word: str) -> list:
	phonetic = phones_for_word(word)
	return map(int, stresses(phonetic[0]).translate({ 50: "0" }) + "0") if phonetic else [0] * (len(word) // 2 + 1)


def flat(arr: map) -> list:
	flattened = []
	for item in arr:
		flattened.extend(item)
	return flattened


def c(row1: tuple, row2: tuple, tau: int) -> int:
	"""

	Function c from the exercise

	:param row1: First row
	:param row2: Second row
	:param tau: Tau parameter
	:return:
	"""

	counter = 0

	for i, value in enumerate(row1):
		if value:
			if 1 in row2[max(0, i - tau):i + 1]:
				counter += 1

	return counter
