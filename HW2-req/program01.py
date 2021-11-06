# -*- coding: utf-8 -*-

def ex(matches: list, k: int) -> list:
	"""

	A function that performs the "Who Screams Louder" game

	:param matches: The list of sequences
	:param k: Parameter K from the game
	:return: A list containing the rankings
	"""

	n_players = len(matches)  # Number of players
	players = []  # Players stats (index, score and sequence sum)
	seqs = []  # Sequences without whitespaces
	whitespace = {  # Ignored characters
		ord(" "): None,
		ord("\t"): None
	}

	# Initialize sequences and stats
	i = 0
	while i < n_players:
		seqs.append(matches[i].translate(whitespace))
		players.append({
			"index": i,
			"score": 0,
			"seq_sum": None
		})
		i += 1

	# Play every match possible
	i = 0
	while i < n_players - 1:
		j = i + 1

		while j < n_players:
			match(seqs[i], seqs[j], players[i], players[j], k)

			j += 1
		i += 1

	sorted_players = sorted(players, key=lambda player: player["score"], reverse=True)  # Sort by score
	return [player["index"] for player in sorted_players]  # Return the original indexes only


def match(seq1: str, seq2: str, player1: dict, player2: dict, k: int) -> None:
	"""

	Compute a match of "Who Screams Louder"

	:param seq1: Player1's sequence
	:param seq2: Player2's sequence
	:param player1: Stats about player1
	:param player2: Stats about player2
	:param k: Parameter K from the game
	:return: None. The winner will have the (stats') score increased
	"""

	points_delta = 0

	i = 0
	length = len(seq1)
	while i < length:

		val_char1 = ord(seq1[i])
		val_char2 = ord(seq2[i])
		val_delta = abs(val_char1 - val_char2)

		if val_delta <= k:
			if val_char1 > val_char2:  # Character 1 wins
				points_delta += 1
			elif val_char2 > val_char1:  # Character 2 wins
				points_delta -= 1
		else:
			if val_char1 < val_char2:  # Character 1 wins
				points_delta += 1
			elif val_char2 < val_char1:  # Character 2 wins
				points_delta -= 1

		i += 1

	# First check: wins whoever has more points
	if points_delta > 0:
		player1["score"] += 1
	elif points_delta < 0:
		player2["score"] += 1

	# Draw: wins whoever has the least sequence total value
	else:

		# Calculate sequence value, if not already done, and store
		if player1["seq_sum"] is None:
			player1["seq_sum"] = seq_sum(seq1)
		if player2["seq_sum"] is None:
			player2["seq_sum"] = seq_sum(seq2)

		sum_seq1 = player1["seq_sum"]
		sum_seq2 = player2["seq_sum"]

		if sum_seq1 < sum_seq2:
			player1["score"] += 1
		elif sum_seq2 < sum_seq1:
			player2["score"] += 1

		# Further draw: win by alphabetic order
		elif seq1 < seq2:
			player1["score"] += 1
		else:
			player2["score"] += 1

	return


def seq_sum(seq: str) -> int:
	"""

	Sums the value of all the characters in a string

	:param seq: The starting string
	:return: The sum of all the characters
	"""

	acc = 0
	for char in seq:
		acc += ord(char)

	return acc
