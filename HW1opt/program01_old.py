# -*- coding: utf-8 -*-

"""
Let int_seq be a string that contains a sequence of non-negative
	integers separated by commas and subtotal a non-negative integer.

Design a function ex1(int_seq, subtotal) that:
	– takes as parameters
	  a string (int_seq) and a positive integer (subtotal >= 0), and
	– returns the number of substrings of int_seq such that
	  the sum of their values is equal to subtotal.

Hint: you can obtain a substring by picking any consecutive
	elements in the original string.

For example, given int_seq = '3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2' and subtotal = 9,
	the function should return 7. The following substrings, indeed, consist of
	values whose sum is equal to 9:
	int_seq = '3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2'
			=> _'0,4,0,3,1,0,1,0'_____________
			   _'0,4,0,3,1,0,1'_______________
			   ___'4,0,3,1,0,1,0'_____________
			   ___'4,0,3,1,0,1'_______________
			   ___________________'0,0,5,0,4'_
			 _____________________'0,5,0,4'_
				 _______________________'5,0,4'_

NOTE: it is FORBIDDEN to use/import any libraries

NOTE: Each test must terminate on the VM before the timeout of
	1 second expires.

WARNING: Make sure that the uploaded file is UTF8-encoded
	(to that end, we recommend you edit the file with Spyder)
"""


def ex1(int_seq: str, subtotal: int) -> int:
	number_list = list(map(int, int_seq.split(",")))
	substrings = 0
	leading_zeroes = 0

	i = 0
	while i < len(number_list):

		acc = 0

		if number_list[i] == 0:
			leading_zeroes += 1
			i += 1
			continue

		j = i
		while j < len(number_list):
			acc += number_list[j]

			j += 1

			if acc == subtotal:
				substrings += 1 + leading_zeroes
			elif acc > subtotal:
				break

		if j == len(number_list):
			break

		leading_zeroes = 0
		i += 1

	return substrings


if __name__ == '__main__':
	print(ex1('3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2', 9))

	pass
