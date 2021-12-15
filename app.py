#3.5 inch = 336 pixels
#2.5 inch = 240 pixels
from PIL import Image
import os
import PIL
import glob

loc = input("Enter file location")
image = Image.open(loc) 
print(image.size)

resized_image = image.resize((240,336)) 
print(resized_image.size)
resized_image.show()
#Source: How to Resize an Image in Python (+ Examples) - Dopinger (https://blog.dopinger.com/how-to-resize-an-image-in-python)

im1 = resized_image.convert('RGB')
dest = input("Enter location to save")
im1.save(dest)