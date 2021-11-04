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
	number_list = list(map(int, int_seq.split(",")))  # Convert the string in a list of integers
	acc = 0  # Result accumulator
	seq_window = []  # Subsequence window
	window_total = 0  # Subsequence window sum
	leading_zeroes = 0  # Ignored zeroes at the start of the window

	for n in number_list:

		# Insert next number into the window and update the total
		seq_window.append(n)
		window_total += n

		# If window's total exceeds the subtotal
		if window_total > subtotal:
			# reset leading zeroes
			leading_zeroes = 0
			# and remove items from the window's start until the total isn't greater than the subtotal
			while window_total > subtotal:
				window_total -= seq_window.pop(0)

		# Remove zeroes from the start of the window (neutral element)
		while len(seq_window) != 0 and seq_window[0] == 0:
			seq_window.pop(0)
			leading_zeroes += 1

		if window_total == subtotal:
			acc += 1 + leading_zeroes

	return acc


if __name__ == '__main__':
	print(ex1('3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2', 9))

	pass
