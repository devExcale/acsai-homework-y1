# -*- coding: utf-8 -*-

from images import save


def ex(data_file_path: str, png_file_path: str, spacing: int) -> tuple:
	"""

	:param data_file_path:
	:param png_file_path:
	:param spacing:
	:return:
	"""

	build_grid = parse_buildings_grid(data_file_path)

	full_width = max(sum(building["width"] for building in row) + spacing * (len(row) + 1) for row in build_grid)
	full_height = sum(max(building["height"] for building in row) for row in build_grid) + spacing * (len(build_grid) + 1)

	image = blank_image(full_width, full_height)

	draw_buildings(image, build_grid, spacing)
	save(image, png_file_path)

	return full_width, full_height


def blank_image(width: int, height: int) -> list:
	"""

	:param width:
	:param height:
	:return:
	"""
	return [[(0, 0, 0)] * width for _ in range(height)]


def draw_buildings(image: list, build_grid: list, spacing: int) -> None:
	"""

	:param image:
	:param build_grid:
	:param spacing:
	:return:
	"""

	width = len(image[0])

	offset_y = 0
	for row in build_grid:
		offset_y += spacing

		row_len = len(row) - 1
		row_height = max(map(lambda b: b["height"], row))
		row_spacing = (width - spacing * 2 - sum(map(lambda b: b["width"], row))) // (row_len if row_len else 2)

		offset_x = spacing
		for building in row:

			if len(row) > 1:
				dh = (row_height - building["height"]) // 2
			else:
				dh = 0
				offset_x += row_spacing

			draw_rect(image, offset_x, offset_y + dh, building)

			offset_x += row_spacing + building["width"]
		offset_y += row_height

	return


def draw_rect(image: list, x: int, y: int, building: dict) -> None:
	"""

	:param image:
	:param x:
	:param y:
	:param building:
	:return:
	"""
	for i in range(building["height"]):
		for j in range(building["width"]):
			image[y + i][x + j] = building["color"]


def parse_buildings_grid(file_path: str) -> list:
	"""

	:param file_path:
	:return:
	"""
	buildings_grid = []

	with open(file_path, "r", encoding="utf-8") as lines:
		for line in lines:
			int_values = list(map(int, filter(None, "".join(line.split()).split(","))))
			buildings_grid.append(list(map(lambda i: {
				"width": int_values[i],
				"height": int_values[i + 1],
				"color": (int_values[i + 2], int_values[i + 3], int_values[i + 4])
			}, range(0, len(int_values) - 4, 5))))

	return buildings_grid
