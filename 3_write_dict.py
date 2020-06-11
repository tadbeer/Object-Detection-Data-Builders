import os
import cv2
import csv
import shutil
import numpy as np
from tqdm import tqdm
import pickle

# writes a dictionary out of the saved annotations csv, 'annot_freq.pickle'
# architecture: {image_1:{class1:num_occurences_class1, class2:num_occurences_class_2}, image2:{},..}

image_dict = {}
class_dict = {}


with open('annotation.csv', 'r') as file:
    reader = csv.reader(file)
    c = 0
    for row in reader:
        img_name, x1, y1, x2, y2, klass = row
        if not img_name in image_dict:
            image_dict[img_name] = {}
            c += 1
            # print(c)
        if not klass in image_dict[img_name]:
            image_dict[img_name][klass] = 0
        if not klass in class_dict:
            class_dict[klass] = 0
        image_dict[img_name][klass] += 1
        class_dict[klass] += 1


with open('annot_freq.pickle', 'wb') as file:
    pickle.dump(image_dict, file, protocol=pickle.HIGHEST_PROTOCOL)


vali = [class_dict[i] for i in class_dict]
vali.sort()
for item in vali:
    for klass in class_dict:
        if class_dict[klass] == item:
            print(klass, item)
