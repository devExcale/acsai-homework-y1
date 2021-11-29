# -*- coding: utf-8 -*-

import images


def ex(data_file_path: str, png_file_path: str, spacing: int) -> None:
	pass


def parse_buildings_grid(file_path) -> list:
	buildings_grid = []

	with open(file_path) as lines:
		line: str
		for line in lines:
			split = line.replace(" ", "").split(",")
			buildings_grid.append(list(map(lambda i: {
				"width": split[i * 5],
				"height": split[i * 5 + 1],
				"color": (split[i * 5 + 2], split[i * 5 + 3], split[i * 5 + 4])
			}, range(len(split) // 5))))

	return buildings_grid


if __name__ == '__main__':
	# place here your personal tests
	pass
