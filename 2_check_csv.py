import os
import cv2
import csv
import shutil
import numpy as np
from tqdm import tqdm
import pickle

#prints rectangles for all annots in csv and displays every interval'th root image

path = 'train'
slice_path = 'slices'
dicty = {}
interval = 10

with open('annotation.csv', 'r') as file:
    reader = csv.reader(file)
    c = 0

    "For verifying the accuracy of annot info contained in csv"
    images=[]
    for row in reader:
        img_name,x1,y1,x2,y2 = row[:-1]
        if not img_name in images:
            if c % interval == 0 and c!=0:
                cv2.imshow('0', image2)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            images.append(img_name)
            image = cv2.imread(os.path.join(path, img_name))
            c += 1
        cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (255, 255, 255), 2)
        # continiously drawing rectangles on the same root_image till a new one is recieved.

        # a copy of root image to be saved each time, cuz rows in csv are for individual annot
        # then when a new root image is encountered, the last saved image is displayed
        image2 = np.copy(image)
