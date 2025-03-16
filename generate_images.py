from PIL import Image
import random
import time
import inspect

# Завантаження зображень
wb1 = Image.open("wb1.png")
gb1 = Image.open("gb1.png")
wb2 = Image.open("wb2.png")
gb2 = Image.open("gb2.png")
wb3 = Image.open("wb3.png")
gb3 = Image.open("gb3.png")
wb4 = Image.open("wb4.png")
gb4 = Image.open("gb4.png")
wb5 = Image.open("wb5.png")
gb5 = Image.open("gb5.png")
wb6 = Image.open("wb6.png")
gb6 = Image.open("gb6.png")
ww1 = Image.open("ww1.png")
gw1 = Image.open("gw1.png")
ww2 = Image.open("ww2.png")
gw2 = Image.open("gw2.png")
ww3 = Image.open("ww3.png")
gw3 = Image.open("gw3.png")
ww4 = Image.open("ww4.png")
gw4 = Image.open("gw4.png")
ww5 = Image.open("ww5.png")
gw5  = Image.open("gw5.png")
ww6 = Image.open("ww6.png")
gw6  = Image.open("gw6.png")
wbg  = Image.open("wbg.png")
gbg = Image.open("gbg.png")

# Створюємо нове зображення потрібного розміру (ширина = сума ширин, висота = однакова)
pw = 62
new_width = pw * 8
new_height = pw * 8
combined_image = Image.new("RGB", (new_width, new_height))

# Вставляємо обидва зображення у нове
combined_image.paste(wb1, (0, 0))
combined_image.paste(gb2, (pw, 0))
combined_image.paste(wb3, (pw * 2, 0))
combined_image.paste(gb4, (pw * 3, 0))
combined_image.paste(wb5, (pw * 4, 0))
combined_image.paste(gb3, (pw * 5, 0))
combined_image.paste(wb2, (pw * 6, 0))
combined_image.paste(gb1, (pw * 7, 0))
combined_image.paste(gb6, (0, pw))
combined_image.paste(wb6, (pw, pw))
combined_image.paste(gb6, (pw * 2, pw))
combined_image.paste(wb6, (pw * 3, pw))
combined_image.paste(gb6, (pw * 4, pw))
combined_image.paste(wb6, (pw * 5, pw))
combined_image.paste(gb6, (pw * 6, pw))
combined_image.paste(wb6, (pw * 7, pw))
combined_image.paste(wbg, (0, pw * 2))
combined_image.paste(gbg, (pw, pw * 2))
combined_image.paste(wbg, (pw * 2, pw * 2))
combined_image.paste(gbg, (pw * 3, pw * 2))
combined_image.paste(wbg, (pw * 4, pw * 2))
combined_image.paste(gbg, (pw * 5, pw * 2))
combined_image.paste(wbg, (pw * 6, pw * 2))
combined_image.paste(gbg, (pw * 7, pw * 2))
combined_image.paste(gbg, (0, pw * 3))
combined_image.paste(wbg, (pw, pw * 3))
combined_image.paste(gbg, (pw * 2, pw * 3))
combined_image.paste(wbg, (pw * 3, pw * 3))
combined_image.paste(gbg, (pw * 4, pw * 3))
combined_image.paste(wbg, (pw * 5, pw * 3))
combined_image.paste(gbg, (pw * 6, pw * 3))
combined_image.paste(wbg, (pw * 7, pw * 3))
combined_image.paste(wbg, (0, pw * 4))
combined_image.paste(gbg, (pw, pw * 4))
combined_image.paste(wbg, (pw * 2, pw * 4))
combined_image.paste(gbg, (pw * 3, pw * 4))
combined_image.paste(wbg, (pw * 4, pw * 4))
combined_image.paste(gbg, (pw * 5, pw * 4))
combined_image.paste(wbg, (pw * 6, pw * 4))
combined_image.paste(gbg, (pw * 7, pw * 4))
combined_image.paste(gbg, (0, pw * 5))
combined_image.paste(wbg, (pw, pw * 5))
combined_image.paste(gbg, (pw * 2, pw * 5))
combined_image.paste(wbg, (pw * 3, pw * 5))
combined_image.paste(gbg, (pw * 4, pw * 5))
combined_image.paste(wbg, (pw * 5, pw * 5))
combined_image.paste(gbg, (pw * 6, pw * 5))
combined_image.paste(wbg, (pw * 7, pw * 5))
combined_image.paste(ww6, (0, pw * 6))
combined_image.paste(gw6, (pw, pw * 6))
combined_image.paste(ww6, (pw * 2, pw * 6))
combined_image.paste(gw6, (pw * 3, pw * 6))
combined_image.paste(ww6, (pw * 4, pw * 6))
combined_image.paste(gw6, (pw * 5, pw * 6))
combined_image.paste(ww6, (pw * 6, pw * 6))
combined_image.paste(gw6, (pw * 7, pw * 6))
combined_image.paste(gw1, (0, pw * 7))
combined_image.paste(ww2, (pw, pw * 7))
combined_image.paste(gw3, (pw * 2, pw * 7))
combined_image.paste(ww4, (pw * 3, pw * 7))
combined_image.paste(gw5, (pw * 4, pw * 7))
combined_image.paste(ww3, (pw * 5, pw * 7))
combined_image.paste(gw2, (pw * 6, pw * 7))
combined_image.paste(ww1, (pw * 7, pw * 7))

# Зберігаємо результат
combined_image.save("generated/test_images/test.png")
print("test image created succesfully")

column = 0
line = 0
list3 = []
index = 0
generated_objects = []

import json

# def convert_to_yolo_format(obj, img_w, img_h):
def convert_to_yolo_format(obj, image_width, image_height):
	class_id = obj['class_id']
	x_min = obj['x_min']
	y_min = obj['y_min']
	x_max = obj['x_max']
	y_max = obj['y_max']
	# Center of the bounding box
	x_center = (x_min + x_max) / 2
	y_center = (y_min + y_max) / 2

	# Обчислюємо центр та розміри об'єкта
	x_center = (x_min + x_max) / 2
	y_center = (y_min + y_max) / 2
	width = x_max - x_min
	height = y_max - y_min

	# Нормалізація
	x_center_norm = x_center / image_width
	y_center_norm = y_center / image_height
	width_norm = width / image_width
	height_norm = height / image_height
	yolo_annotation = f"{class_id} {x_center_norm} {y_center_norm} {width_norm} {height_norm}"

	return yolo_annotation

import os
import random
import inspect

def main():
	chess = Image.new("RGB", (62 * 8, 62 * 8))
	global column, line, list3, index
	column, line = 0, 0
	list3 = []

	# Обмеження використання фігур
	restrictions = {
		'b1': (2, 0), 'b2': (2, 0), 'b3': (2, 0), 'b4': (1, 0), 'b5': (1, 0), 'b6': (8, 0),
		'w1': (2, 0), 'w2': (2, 0), 'w3': (2, 0), 'w4': (1, 0), 'w5': (1, 0), 'w6': (8, 0), 'bg': (40, 0)
	}

	# Списки фігур
	list1 = [gb1, gb2, gb3, gb4, gb5, gb6, gw1, gw2, gw3, gw4, gw5, gw6, gbg, gbg, gbg, gbg]
	list2 = [wb1, wb2, wb3, wb4, wb5, wb6, ww1, ww2, ww3, ww4, ww5, ww6, wbg, wbg, wbg, wbg]
	
	variables = {
		'gb1': gb1, 'gb2': gb2, 'gb3': gb3, 'gb4': gb4, 'gb5': gb5, 'gb6': gb6,
		'gw1': gw1, 'gw2': gw2, 'gw3': gw3, 'gw4': gw4, 'gw5': gw5, 'gw6': gw6,
		'gbg': gbg, 'wb1': wb1, 'wb2': wb2, 'wb3': wb3, 'wb4': wb4, 'wb5': wb5, 'wb6': wb6,
		'ww1': ww1, 'ww2': ww2, 'ww3': ww3, 'ww4': ww4, 'ww5': ww5, 'ww6': ww6, 'wbg': wbg
	}
	annotation = {
		'gb1': 0, 'gb2': 1, 'gb3': 2, 'gb4': 3, 'gb5': 4, 'gb6': 5,
		'gw1': 6, 'gw2': 7, 'gw3': 8, 'gw4': 9, 'gw5': 10, 'gw6': 11, 'gbg': 12,
		'wb1': 0, 'wb2': 1, 'wb3': 2, 'wb4': 3, 'wb5': 4, 'wb6': 5,
		'ww1': 6, 'ww2': 7, 'ww3': 8, 'ww4': 9, 'ww5': 10, 'ww6': 11, 'wbg': 12,
		'chess_table': 13
	}
	while column < 8:
		list3 = []
		for line in range(8):
			selected = None
			while selected is None:
				if line % 2 == column % 2:
					selected = random.choice(list2)
				else:
					selected = random.choice(list1)
				
				for name, data in variables.items():
					if id(selected) == id(data):  # Порівняння через id()
						figure_key = name[-2:] if name[-2:] in restrictions else name
						max_count, current_count = restrictions.get(figure_key, (1, 0))

						if current_count >= max_count:
							selected = None  # Потрібно вибрати іншу фігуру
						else:
							restrictions[figure_key] = (max_count, current_count + 1)
							list3.append(name)
							break

		for line, obj in enumerate(list3):
			obj_image = variables[obj]
			chess.paste(obj_image, (62 * line, 62 * column))
			# print(f"Pasted {obj} at ({62 * line}, {62 * column})")
			generated_objects.append({"class_id": annotation[obj], "x_min": 62 * line + 174, "y_min": 62 * column + 112, "x_max": 62 * line + 62 + 174, "y_max": column * 62 + 62 + 112})
		data = {"class_id": 13, "x_min": 174, "y_min": 112, "x_max": 62 * 8 + 174, "y_max": 8 * 62 + 112}
		if data not in generated_objects:
				generated_objects.append({"class_id": 13, "x_min": 174, "y_min": 112, "x_max": 62 * 8 + 174, "y_max": 8 * 62 + 112})
		label_path = os.path.join("C:/Users/Admin/Pictures/dataset_maker/data", "annotations", f"{index}_template.txt")
		with open(label_path, "w") as f:
			for obj in generated_objects:
				f.write(convert_to_yolo_format(obj, 1053, 684) + "\n")
		column += 1
	chess.save(f"generated/{index}.png")
	print(f"picture {index}.png saved")
	index += 1	
		# 	elif line in [2, 4, 6, 8]:
		# 		# List 1 - handle list 1 selection if necessary
		# 		pass
		# 	else:
		# 		print(f"Error in column {column}, line {line}")
		# elif column in [2, 4, 6, 8]:
		# 	if line in [1, 3, 5, 7]:
		# 		# Handle list 1 selection for columns 2, 4, 6, 8
		# 		pass
		# 	elif line in [2, 4, 6, 8]:
		# 		# Handle list 2 selection for columns 2, 4, 6, 8
		# 		pass
		# 	else:
		# 		print(f"Error in column {column}, line {line}")
		# else:
		# 	print(f"Error in column {column}, line {line}")

# Відображаємо зображення
# combined_image.show()
def create_image():
	def_index = index - 1
	img = Image.new("RGB", (1053, 684))
	template = Image.open("template.png")
	generated = Image.open(f"generated/{def_index}.png")
	img.paste(template, (0, 0))
	img.paste(generated, (174, 112))
	img.save(f"data/images/{def_index}_template.png")
	os.remove(f"generated/{def_index}.png")
	
index = int(input(": "))
while True:
	main()
	create_image()