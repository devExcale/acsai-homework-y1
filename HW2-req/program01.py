# -*- coding: utf-8 -*-

def ex(matches: list, k: int) -> list:
	"""

	A function that performs the "Who Screams Louder" game

	:param matches: The list of sequences
	:param k: Parameter K from the game
	:return: A list containing the rankings
	"""

	n_players = len(matches)  # Number of players

	# Initialize sequences and stats
	players = tuple({
		"index": i,
		"score": 0,
		"seq_ints": tuple(ord(char) for char in match if char != " " and char != "\t"),
		"seq_sum": None
	} for i, match in enumerate(matches))

	for i in range(n_players - 1):
		for j in range(i + 1, n_players):
			do_match(players[i], players[j], k)

	sorted_players = sorted(players, key=lambda player: player["score"], reverse=True)  # Sort by score
	return [player["index"] for player in sorted_players]  # Return the original indexes only


def do_match(player1: dict, player2: dict, k: int) -> None:
	"""

	Compute a match of "Who Screams Louder"

	:param player1: Player1's stats
	:param player2: Player2's stats
	:param k: Parameter K from the game
	:return: None, the function assigns the point automatically
	"""

	points_delta = 0
	obliterate_sign = abs  # A little trick to make the program faster

	# Loop both sequences in parallel
	# for i in range(len(player1["seq_ints"])):
	for val_char1, val_char2 in zip(player1["seq_ints"], player2["seq_ints"]):

		# val_char1 = player1["seq_ints"][i]
		# val_char2 = player2["seq_ints"][i]
		val_delta = obliterate_sign(val_char1 - val_char2)  # Yup, here's the trick

		if val_delta <= k:
			if val_char1 > val_char2:  # Character 1 points++
				points_delta += 1
			elif val_char2 > val_char1:  # Character 2 points++
				points_delta -= 1
		else:
			if val_char1 < val_char2:  # Character 1 points++
				points_delta += 1
			elif val_char2 < val_char1:  # Character 2 points++
				points_delta -= 1

	assign_point(player1, player2, points_delta)  # Assign match point

	return


def assign_point(player1: dict, player2: dict, points_delta: int) -> None:
	"""

	Check, by the rules of "Who Screams Louder",
	which of the two players gets the match point.

	:param player1: Player1's stats
	:param player2: Player2's stats
	:param points_delta: The difference in points between the two players
	:return: None, the function assigns the point automatically
	"""

	# First check: wins whoever has more points
	if points_delta > 0:
		player1["score"] += 1
	elif points_delta < 0:
		player2["score"] += 1

	# Draw: wins whoever has the least sequence total value
	else:

		# Calculate sequence value, if not already done, and store
		if not player1["seq_sum"]:
			player1["seq_sum"] = sum(player1["seq_ints"])
		if not player2["seq_sum"]:
			player2["seq_sum"] = sum(player2["seq_ints"])

		sum_seq1 = player1["seq_sum"]
		sum_seq2 = player2["seq_sum"]

		if sum_seq1 < sum_seq2:
			player1["score"] += 1
		elif sum_seq2 < sum_seq1:
			player2["score"] += 1

		# Further draw: win by alphabetic order
		elif player1["seq_ints"] < player2["seq_ints"]:
			player1["score"] += 1
		else:
			player2["score"] += 1

	return
