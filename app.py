#3.5 inch = 336 pixels
#2.5 inch = 240 pixels
#3 x 1 = 720 wide
#note for incomplete pages. have a 2.5 x3.5 white image. copy it the number\
#  of times needed to get to 9 then paste those white images so we have 9 pics left
from PIL import Image
import os
import PIL
import glob

loc = input("Enter file location")
files = os.listdir(loc)
images = [Image.open(os.path.join(loc, x)) for x in files]
total_width = 0
max_height = 0
#newimage = images[0].resize(240,336)
# find the width and height of the final image
threepics = []
for i in range(len(images)):
    #resize first
    images[i] = images[i].resize((240,336))
    total_width += images[i].size[0]
    max_height = max(max_height, images[i].size[1])
    
print(str(total_width) + ', ' + str(max_height))

# create 3x1 new image with the appropriate height and width
new_img = Image.new('RGB', (total_width, max_height))
# Write the contents of the new image
current_width = 0
for img in images:
  new_img.paste(img, (current_width,0))
  current_width += img.size[0]
  if total_width == 720:
    threepics.append(new_img)
# Save the image
new_img.save('NewImage.jpg')

new_img.show()

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