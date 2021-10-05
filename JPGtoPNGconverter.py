# build to use at terminal
# python 3 JPGtoPNGconverter.py Pokedex\ new\

import sys
import os
from PIL import Image
import pdb

#grab the first and second argument
#home = r'C:\Users\Julie\Pycharm projects\image-playground'
fold1 = sys.argv[1]
fold2 = sys.argv[2]


#check if .\new\ exists, and if not create it
if not os.path.isdir(fold2):
    os.mkdir(fold2)


#loop through Pokedex,
for i in os.listdir(fold1):
    img_path = os.path.join(fold1, i)
    convert_path =os.path.join(fold2, i[:-4] + '.png')
    img = Image.open(img_path)

    #convert images to png
    #save to the new folder
    img.save(convert_path, 'png')