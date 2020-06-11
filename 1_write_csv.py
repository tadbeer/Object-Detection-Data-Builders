import os
import cv2
import shutil
from tqdm import tqdm
import csv

min_side = 800
max_side = 1333

path = 'train'      #root images path, where all the annotated images are kept
slice_path = 'slices'
c = 0

soochi = {}  # list of all classes
for folder in os.listdir(slice_path):
    soochi[folder] = 0

datta = []  # array to hold all the data
# Shall pick one root image and scavanenge all the respective classes folders for all the annots in this image.

for file in tqdm(os.listdir(path)):
    try:
        naam = file[:-4] 
        img_path = os.path.join(path, file)
        image = cv2.imread(img_path)

        for folder in os.listdir(slice_path):
            folder_path = os.path.join(slice_path, folder)
            for slicy in os.listdir(folder_path):
                image_naam = slicy.split('@')[0]
                if image_naam == naam:
                    _, x1, y1, x2, y2 = slicy[:-4].split('@')
                    array = [file, int(x1), int(y1), int(x2), int(y2), folder]
                    datta.append(array)
                    soochi[folder] += 1

    except Exception as e:
        print(e)
        print(file)

with open('annotation.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(datta)