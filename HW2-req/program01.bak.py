# -*- coding: utf-8 -*-

""" In the game "who screams louder," two players A and B, generate
sequences of variable length values. Each value is represented by a
single character. The sequences can be of different lengths because
the values can be separated by one (or more) whitespaces
and tabs ('\t'). The number of non-space characters is, however, equal
for each sequence.

Each element of the sequence of A is compared with the corresponding
element of the B's sequence, and a point is assigned:
- to the player who generated the highest value (for example A), if
  the difference between the value of A and the value of B is less
  than or equal to a parameter k decided at the beginning of the
  challenge
- to the player who has generated the lowest value (for example B), if
  the difference between the value of A and the value of B is greater
  than k (i.e., A has failed)
- to none, in case of a tie.
At the end of the assignment, whoever scored the most points wins. In
the case of a tie, the player who generated the sequence with the
lower total sum of values wins. In the case of a further tie, the
player with the first sequence in lexicographic order wins. It cannot
happen that two players generate precisely the same sequence of
values.

It is necessary to create a function that evaluates the ranking of a
"who screams louder" tournament. The function takes as input a list of
strings and a k parameter, and returns the final ranking of the
tournament, as a list. The string in position "i" in the input list
corresponds to the player "i"'s sequence of values.  In the
tournament, each player challenges all the others with their own
sequence: thus, if there are n players, each player will make n-1
challenges. The number of winning challenges determines the position in
the ranking. In case of a tie, the players are ordered according to
their initial position.

Example of "who screams louder" tournaments between three players.

	If k=2 and the list is ["aac", "ccc", "caa"], then
		the challenge 0, 1 is won by 1 by 2 points to 0, since the
			difference between "c" and "a" is less than or equal to 2
		the challenge 0, 2 is a 1 to 1 draw, the two sequences have
			equal sum, but 0 wins because "aac" < "caa"
		the challenge 1, 2 is won by 1 by 2 points to 0, since the
			difference between "c" and "a" is less than or equal to 2.

		In the end 0 has 1 challenge, 1 has 2 challenges and 2 has 0
			challenges, so the final ranking will be [1, 0, 2].

	If k=1 and the list is ["aac", "ccc", "caa"], then
		the challenge 0, 1 is won by 0 by 2 points to 0, since the
			difference between "c" and "a" is greater than 1
		the challenge 0, 2 is a 1 to 1 tie, the two sequences have
			equal sum equal, but 0 wins because "aac" < "caa".
		the challenge 1, 2 is won by 2 for 2 points to 0, since the
			difference between "c" and "a" is greater than 1.

		In the end 0 has 2 challenges, 1 has 0 challenges and 2 has 1
			challenge, so the final ranking will be [0, 2, 1].

	If k=10 and the list is [ "abc", "dba" , "eZo"], then
		the challenge 0, 1 is a tie, but 0 wins because its sequence
			has lower sum
		the challenge 0, 2 is won by 0 by 2 points to 1, because 2 is
			wrong with the letter 'o' against 'c'
		the challenge 1, 2 is won by 1 for 2 points to 1, because 2 is
			fails with the letter 'o' vs. 'a'.

		In the end 0 has 2 challenges, 1 has 1 challenge and 2 has 0
			challenges, so the final ranking will be [0, 1, 2].

	If k=50 and the list is [ "A ƐÈÜ", "BEAR" , "c Ʈ ´ ."]
		Challenge 0, 1 is won by 1 by 4 points to 0.
		Challenge 0, 2 is won by 2 for 3 points to 1.
		Challenge 1, 2 is won by 1 by 3 points to 1.
		In the end 0 has 0 challenges, 1 has 1 challenge and 2 has 2
		challenges, so the final ranking will be [1, 2, 0].

Each test is run with a 6s timeout (*2 on the VM)

"""


def ex(matches: list, k: int) -> list:
	"""

	A function that performs the "Who Screams Louder" game

	:param matches: The list of sequences
	:param k: Parameter K
	:return: A list containing the rankings
	"""

	nowhite_matches = []

	n_matches = len(matches)
	scores = [[i, 0] for i in range(n_matches)]

	i = 0
	while i < n_matches:
		nowhite_matches.append(remove_whitespace(matches[i]))
		i += 1

	i = 0
	while i < n_matches - 1:
		j = i + 1

		while j < n_matches:
			indexes = [i, j]

			seq1 = nowhite_matches[i]
			seq2 = nowhite_matches[j]

			match_result = match(seq1, seq2, k)
			index = indexes[match_result]
			scores[index][1] += 1

			j += 1

		i += 1

	sorted_scores = sorted(scores, key=lambda tup: tup[1], reverse=True)
	return [tup[0] for tup in sorted_scores]


def match(seq1: str, seq2: str, k: int) -> int:
	"""

	Compute a match of "Who Screams Louder"

	:param seq1: First sequence
	:param seq2: Second sequence
	:param k: Parameter K
	:return: 0 if seq1 wins, 1 otherwise
	"""

	# TODO Optimization: can just use positive/negative counter (scores seq1 add, scores seq2 sub)
	point_seq1 = 0
	point_seq2 = 0

	i = 0
	length = len(seq1)
	while i < length:

		oseq1 = ord(seq1[i])
		oseq2 = ord(seq2[i])
		delta = abs(oseq1 - oseq2)

		if delta <= k:
			if oseq1 > oseq2:
				point_seq1 += 1
			elif oseq2 > oseq1:
				point_seq2 += 1
		else:
			if oseq1 < oseq2:
				point_seq1 += 1
			elif oseq2 < oseq1:
				point_seq2 += 1

		i += 1

	if point_seq1 > point_seq2:
		return 0
	elif point_seq2 > point_seq1:
		return 1

	# TODO Optimization: store sum_seq in a record
	sum_seq1 = sum_seq(seq1)
	sum_seq2 = sum_seq(seq2)

	if sum_seq1 < sum_seq2:
		return 0
	elif sum_seq2 < sum_seq1:
		return 1

	if seq1 < seq2:
		return 0
	else:
		return 1


def sum_seq(seq: str) -> int:
	"""

	Sums the value of all the characters in a string

	:param seq: The starting string
	:return: The sum of all the characters
	"""

	acc = 0
	for char in seq:
		acc += ord(char)

	return acc


def remove_whitespace(seq: str) -> str:
	"""

	Removes all whitespace from a string

	:param seq: The starting string
	:return: The no-whitespace string
	"""

	whitespace = {
		ord(" "): None,
		ord("\t"): None
	}

	return seq.translate(whitespace)
