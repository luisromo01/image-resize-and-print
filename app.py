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
std_width = 240
total_width = 720 
max_height = 336 
#newimage = images[0].resize(240,336)
# find the width and height of the final image
threepics = []
for i in range(len(images)):
    #resize first
    images[i] = images[i].resize((240,336))
    
#print(str(total_width) + ', ' + str(max_height))

# create 3x1 new image with the appropriate height and width
new_img = Image.new('RGB', (std_width, max_height))
# Write the contents of the new image
current_width = 0
new_img = Image.new('RGB', (total_width, max_height))
for img in images:
  new_img.paste(img, (current_width,0))
  current_width += img.size[0]
  if current_width == 720:
    threepics.append(new_img)
    new_img = Image.new('RGB', (total_width, max_height))
    print(len(threepics))
    current_width = 0
# Save the image
# new_img.save('NewImage.jpg')

threepics[0].show()
threepics[1].show()
threepics[0].save('test1.jpg')
threepics[1].save('test2.jpg')
threepics[2].save('test3.jpg')
#will now paste vertically

#stacked = threepics[0].paste(threepics[1],(total_width, 3* max_height))
stacked = Image.new('RGB', (720, 336*3))
current_height = 0
for img in threepics:
  stacked.paste(img, (0,current_height))
  current_height += img.size[1]
stacked.save('stacked.jpg')
#  if current_height == 336 * 3:
#    threepics.append(new_img)
#    new_img = Image.new('RGB', (total_width, max_height))
#    print(len(threepics))
#    current_width = 0
#

#threepics[0].save('stacked.jpg')

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