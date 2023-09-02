#!/usr/bin/env python3

from PIL import Image
from glob import glob
import os

for file in glob('ic_*'):
    image = Image.open(file).convert('RGB')
    path, filename = os.path.split(file)
    filename = os.path.splitext(filename)[0]
    image.rotate(270).resize((128, 128)).save('/opt/icons/{}.jpeg'.format(filename))

print('Ok')
