# -*- coding: utf-8 -*-

from images import save


def ex(data_file_path: str, png_file_path: str, spacing: int) -> tuple:
	"""

	"""

	build_grid = parse_buildings_grid(data_file_path)

	inner_width = max(sum(building["width"] for building in row) + spacing * (len(row) - 1) for row in build_grid)
	inner_height = sum(max(building["height"] for building in row) for row in build_grid) + spacing * (len(build_grid) - 1)

	full_width = inner_width + spacing * 2
	full_height = inner_height + spacing * 2

	map(print, build_grid)
	for row in build_grid:
		print(row)
	print(f"Inner Width: {inner_width}")
	print(f"Inner Height: {inner_height}")
	print(f"Full Width: {full_width}")
	print(f"Full Height: {full_height}")

	image = [[(0, 0, 0) for _ in range(full_width)] for _ in range(full_height)]

	draw_buildings(image, build_grid, spacing)
	save(image, png_file_path)

	return full_width, full_height


def draw_buildings(image: list, build_grid: list, spacing: int) -> None:
	"""

	"""

	width = len(image[0])

	offset_y = 0
	for row in build_grid:
		offset_y += spacing

		row_height = max(b["height"] for b in row)
		row_spacing = (width - spacing * 2 - sum(b["width"] for b in row)) // (len(row) - 1 if len(row) > 1 else 2)

		offset_x = spacing
		for building in row:

			if len(row) > 1:
				dh = (row_height - building["height"]) // 2
			else:
				dh = 0
				offset_x += row_spacing

			for i in range(building["height"]):
				for j in range(building["width"]):
					image[offset_y + dh + i][offset_x + j] = building["color"]

			offset_x += row_spacing + building["width"]
		offset_y += row_height

	return


def parse_buildings_grid(file_path: str) -> list:
	"""

	"""

	buildings_grid = []

	with open(file_path, "r", encoding="utf-8") as lines:
		for line in lines:
			int_values = list(map(int, filter(None, "".join(line.split()).split(","))))
			buildings_grid.append(list(map(lambda i: {
				"width": int_values[i * 5],
				"height": int_values[i * 5 + 1],
				"color": (int_values[i * 5 + 2], int_values[i * 5 + 3], int_values[i * 5 + 4])
			}, range(len(int_values) // 5))))

	return buildings_grid
