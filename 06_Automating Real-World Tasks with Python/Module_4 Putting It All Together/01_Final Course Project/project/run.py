#! /usr/bin/env python3

import os
import requests
import re

desc_path = 'supplier-data/descriptions/' 
image_path = 'supplier-data/images/'

text_files = sorted(os.listdir(desc_path))
jpeg_images = sorted([image_name for image_name in os.listdir(image_path) if '.jpeg' in image_name])

list_content = []
image_counter = 0

for file in text_files:
    format = ['name', 'weight', 'description']
    
    with open(desc_path + file, 'r') as f:
        data = {}
        contents = f.read().split("\n")[0:3]
        
        contents[1] = int((re.search(r'\d+', contents[1])).group())
        
        counter = 0
        for content in contents:
            data[format[counter]] = content
            counter += 1
        
        data['image_name'] = jpeg_images[image_counter]
        
        list_content.append(data)
        image_counter +=1

# print(list_content)

for item in list_content:
    resp = requests.post('http://127.0.0.1:80/fruits/', json=item)
    if resp.status_code != 201:
        raise Exception('POST error status={}'.format(resp.status_code))
    print('Created feedback ID: {}'.format(resp.json()["id"]))
