# -*- coding: utf-8 -*-

# noinspection PyPep8Naming
# because can't rename parameters
def ex(colors: list, D: int, img_properties: str) -> list:
	"""

	:param colors:
	:param D:
	:param img_properties:
	:return:
	"""

	if D == 1:
		return [((colour,),) for colour in colors]

	new_images = []
	images = ex(colors, D - 1, img_properties)
	for image in images:
		if img_properties == "pattern_diff_":
			new_images.extend(pattern_diff(image, colors))
		elif img_properties == "pattern_cross_":
			new_images.extend(pattern_cross(image, colors))
		elif img_properties == "pattern_hrect_":
			new_images.extend(pattern_hrect(image, colors))
		elif img_properties == "pattern_vrect_":
			new_images.extend(pattern_vrect(image, colors))
		else:
			new_images.extend(pattern_none(image, colors))

	return new_images


def pattern_none(image: list, colours: list, slider: int = -1) -> list:
	"""

	Extends the image by 1 pixel, using the provided colours
	and **no** pattern.

	:param slider:
	:param image: A list of lists, which is the image matrix
	:param colours: A list of colours
	:return: A list with all the possible images
	"""

	new_images = []

	if slider == 0:
		new_image = [list(row) for row in image]
		for row in new_image:
			row.append(-1)
		new_image.append([-1 for _ in range(len(image) + 1)])
		new_images.append(new_image)

	elif slider < 0:		# function entry point
		return list(map(lambda img: tuple(map(tuple, img)), pattern_none(image, colours, len(image) * 2 + 1)))

	else:
		images = pattern_none(image, colours, slider - 1)
		side = len(images[0])

		if slider < side:
			for img in images:
				for colour in colours:
					new_image = [row.copy() for row in img]
					new_image[slider - 1][side - 1] = colour
					new_images.append(new_image)
		else:
			for img in images:
				for colour in colours:
					new_image = [row.copy() for row in img]
					new_image[side - 1][slider - side] = colour
					new_images.append(new_image)

	return new_images


def pattern_diff(image: list, colours: list, slider: int = -1) -> list:
	"""

	Extends the image by 1 pixel, using the provided colours
	and the *diff* pattern.

	:param slider:
	:param image: A list of lists, which is the image matrix
	:param colours: A list of colours
	:return: A list with all the possible images
	"""

	new_images = []

	if slider == 0:
		new_image = [list(row) for row in image]
		for row in new_image:
			row.append(-1)
		new_image.append([-1 for _ in range(len(image) + 1)])
		new_images.append(new_image)

	elif slider < 0:		# function entry point
		return list(map(lambda img: tuple(map(tuple, img)), pattern_none(image, colours, len(image) * 2 + 1)))

	else:
		images = pattern_none(image, colours, slider - 1)
		side = len(images[0])

		if slider < side:
			for img in images:
				for colour in colours:

					forbidden_colours = []
					if slider > 1:
						forbidden_colours.extend(img[slider - 2][side - 2:side])
					forbidden_colours.append(img[slider - 1][side - 2])
					forbidden_colours.append(img[slider][side - 2])

					print(f"[{colour}]: {forbidden_colours}")

					if colour in forbidden_colours:
						continue

					new_image = [row.copy() for row in img]
					new_image[slider - 1][side - 1] = colour
					new_images.append(new_image)
		else:
			for img in images:
				for colour in colours:

					forbidden_colours = img[side - 2][max(0, slider - side - 1):slider - side + 2]
					if slider > side:
						forbidden_colours.append(img[side - 1][slider - side - 1 ])

					print(f"[{colour}]: {forbidden_colours}")

					if colour in forbidden_colours:
						continue

					new_image = [row.copy() for row in img]
					new_image[side - 1][slider - side] = colour
					new_images.append(new_image)

	return new_images


def pattern_cross(image: list, colours: list) -> list:
	"""

	Extends the image by 1 pixel, using the provided colours
	and the *cross* pattern.

	:param image: A list of lists, which is the image matrix
	:param colours: A list of colours
	:return: A list with all the possible images
	"""

	new_images = []
	side = len(image)

	colour1 = image[0][0]
	colour2s = [image[0][1]] if side > 1 else [c for c in colours if c != colour1]

	for colour2 in colour2s:

		# TODO: optimization: this pattern is just two alternating rows
		new_image = tuple(image[i] + (colour1 if (i + len(image[i])) % 2 == 0 else colour2,) for i in range(side))
		new_image += (tuple(colour1 if (j + side) % 2 == 0 else colour2 for j in range(side + 1)),)

		new_images.append(new_image)

	return new_images


def pattern_hrect(image: tuple, colours: list) -> list:
	"""

	Extends the image by 1 pixel, using the provided colours
	and the *hrect* pattern.

	:param image: A tuple of tuples, which is the image matrix
	:param colours: A list of colours
	:return: A list with all the possible images
	"""

	new_images = []
	side = len(image)

	for colour in colours:
		if image[side - 1][0] != colour:

			new_image = tuple(image[i] + (image[i][0],) for i in range(side))
			new_image += (tuple(colour for _ in range(side + 1)),)

			new_images.append(new_image)

	return new_images


def pattern_vrect(image: tuple, colours: list) -> list:
	"""

	Extends the image by 1 pixel, using the provided colours
	and the *vrect* pattern.

	:param image: A tuple of tuples, which is the image matrix
	:param colours: A list of colours
	:return: A list with all the possible images
	"""

	new_images = []
	side = len(image)

	for colour in colours:
		if image[0][side - 1] != colour:

			new_image = tuple(image[i] + (colour,) for i in range(side))
			new_image += (tuple(new_image[0][j] for j in range(side + 1)),)

			new_images.append(new_image)

	return new_images


if __name__ == '__main__':
	a = pattern_diff(((0,),), [0, 25, 50, 255])
	for img in a:
		print("-----")
		for row in img:
			print(row)
