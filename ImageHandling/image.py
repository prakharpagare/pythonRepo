from PIL import Image, ImageFilter, ImageEnhance
import sys
import os

sour = sys.argv[1]
dest = sys.argv[2]

if (not os.path.exists(dest)):
	os.mkdir(dest)

for file_name in os.listdir(sour):	
	file = Image.open(f"{sour}{file_name}")
	file.filter(ImageFilter.BLUR)
	enhanser = ImageEnhance.Brightness(file)
	outFile = enhanser.enhance(1.5)
	outFile = outFile.rotate(180)
	outFile.save(f"{dest}{file_name}.png",'png')
