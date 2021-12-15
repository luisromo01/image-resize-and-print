#3.5 inch = 336 pixels
#2.5 inch = 240 pixels
from PIL import Image
import os
import PIL
import glob

loc = input("Enter file location")
image = Image.open(loc) 
print(image.size)


