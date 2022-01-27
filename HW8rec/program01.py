#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from images import load as load_img, save as save_img


def ex1(input_file: str, output_file: str) -> int:
	img = load_img(input_file)

	colours = [img[0][0]]
	res = count_plots(img, colours, len(img[0]), len(img))

	save_img([colours], output_file)

	return res


def count_plots(img: list, colours: list, end_h: int, end_v: int, start_h: int = 0, start_v: int = 0) -> int:
	divs = find_divs(img, colours[0], end_h, end_v, start_h, start_v)
	count = 0

	if divs:
		colours.append(divs[2])
		count += count_plots(img, colours, end_h, end_v, divs[0] + 1, divs[1] + 1)  # SE
		count += count_plots(img, colours, divs[0], end_v, start_h, divs[1] + 1)  # SW
		count += count_plots(img, colours, end_h, divs[1], divs[0] + 1, start_v)  # NE
		count += count_plots(img, colours, divs[0], divs[1], start_h, start_v)  # NW

	else:
		count = 1

	return count


def find_divs(img: list, bg: tuple, end_h: int, end_v: int, start_h: int, start_v: int) -> tuple:
	"""

	:param img:
	:param bg:
	:param end_h: [exclusive]
	:param end_v:
	:param start_h: [inclusive]
	:param start_v:
	:return: A tuple (x: int, y: int, colour: tuple) containing coords and colour of the divisor if found, an empty tuple otherwise
	"""

	for y in range(start_v, end_v):

		if img[y][start_h] != bg:
			div_colour = img[y][start_h]

			if all(pixel == div_colour for pixel in img[y][start_h:end_h]):
				# Horizontal divisor here for current superplot
				for x, pixel in enumerate(img[start_v][start_h:end_h], start_h):
					if pixel == div_colour:
						return x, y, div_colour

	return tuple()


if __name__ == '__main__':
	img = load_img("puzzles/hard01.in.png")

	bg = img[0][0]
	colours = [bg]

	print(count_plots(img, colours, len(img), len(img[0])))

	for colour in colours:
		print(colour)
