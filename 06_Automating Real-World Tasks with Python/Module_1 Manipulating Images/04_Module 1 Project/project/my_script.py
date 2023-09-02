#!/usr/bin/env python3

from PIL import Image
import os

# write full path to the images folder in the variable 'source_images_dir'
source_images_dir = os.path.abspath(os.getcwd()) + '/images'

# create list of  all files of an images folder
images_list = [file for file in os.listdir(source_images_dir) if os.path.isfile(os.path.join(source_images_dir, file))]

print(images_list)

# folder for the converted images
folder = '/opt/icons/'

for image in images_list:
    print(image)
    #im = Image.open(image)
    #im.rotate(90).resize((128,128)).save(folder + image)

