# -*- coding: utf-8 -*-

from pronouncing import phones_for_word, stresses
from math import sqrt


# noinspection PyPep8Naming
def PoemSync(input_file: str, output_file: str, tau: int) -> float:
	rows: list
	matrix = []
	adict = {ord("2"): "0"}

	with open(input_file, "r") as input_stream:
		rows = list(map(normify_string, input_stream.readlines()))

	row: str
	for row in rows:
		v = []
		matrix.append(v)

		for word in row.split(" "):
			phonetic = phones_for_word(word)

			if phonetic:
				a = map(int, stresses(phonetic[0] + "0").translate(adict))
			else:
				a = [0] * (len(word) // 2 + 1)

			v.extend(a)

	max_len = max(map(len, matrix))
	for v in matrix:
		v.extend([0] * (max_len - len(v)))

	syncs = []
	matrix_len = len(matrix)
	for row1 in matrix:
		for row2 in matrix:
			if row1 is row2:
				break
			root = sqrt(sum(row1) * sum(row2))
			if root:
				syncs.append(0.5 / root * (c(row1, row2, tau) + c(row2, row1, tau)))
			else:
				syncs.append(0)

	for row in matrix:
		print(row)

	return round(sum(syncs) / matrix_len, 6)


# print(rows)
# word_matrix = list(map(str.split, rows))
# word_matrix = list(map(lambda word: list(map(phones_for_word, word)), word_matrix))
# print(word_matrix)
# word_matrix = list(map(lambda phones: phones[0] if phones else [], word_matrix))
# print(matrix)


def get_accents(s: str) -> list:
	phonetic = phones_for_word(s)
	return list(map(int, stresses(phonetic[0]))) if phonetic else [0] * (len(s) // 2)


def normify_string(string: str) -> str:
	return "".join(char if char.isalpha() or char == " " else " " if char == "'" else "" for char in string)


def c(row1: list, row2: list, tau: int) -> int:
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


def m(row: tuple) -> int:
	return sum(row)


if __name__ == '__main__':
	# TODO: file print
	print(PoemSync("poems/example.txt", "", 2))
	# a = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
	# b = [1, 0, 0, 0, 1, 0, 1, 0, 1, 0]
	# tau = 2
	# ab = c(a, b, tau)
	# ba = c(b, a, tau)
	# ma = sum(a)
	# mb = sum(b)
	# root = (sqrt(ma * mb))
	# sync = 0.5 * (ab + ba) / root
	# print(f"c(a|b): {ab}\nc(b|a): {ba}\nm(a): {ma}\nm(b): {mb}\nsqrt(m(a) * m(b)): {root}\nsync: {sync}")
