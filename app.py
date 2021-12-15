#3.5 inch = 336 pixels
#2.5 inch = 240 pixels
from PIL import Image
import os
import PIL
import glob

loc = input("Enter file location")
files = os.listdir(loc)
images = [Image.open(x) for x in files]
total_width = 0
max_height = 0
# find the width and height of the final image
for img in images:
    #resize first
    img.resize(240,336)
    total_width += img.size[0]
    max_height = max(max_height, img.size[1])
    
print(total_width + ', ' + ma_height)

#resized_image = image.reskze((240,336)) 
#print(resized_image.size)
#resized_image.show()
##Source: How to Resize an Image in Python (+ Examples) - Dopinger (https://blog.dopinger.com/how-to-resize-an-image-in-python)
#images = [Image.open(x) for x in ['path/to/image1', '/path/to/image2']]
#total_width = 0
#max_height = 0
## find the width and height of the final image
#for img in images:
#    total_width += img.size[0]
#    max_height = max(max_height, img.size[1])
##turn image into pdf
#im1 = resized_image.convert('RGB')
#dest = input("Enter location to save")
#im1.save(dest)