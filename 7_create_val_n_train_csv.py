import csv
import os

#creates separate csv files for train and validation data

#put the name of the 'txt' file generated in the previous step as 'val_list_path'

root_ims_annotation_csv_path = 'annotation.csv'
val_list_path = 'val_abs_0.196.txt'

train_path = 'train'
val_path = 'validn'

val_list = []

with open(val_list_path, 'r') as file:
    for line in file:
        val_list.append(line[:-1])

train_annot_list = []
val_annot_list = []

with open(root_ims_annotation_csv_path, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        img_name, _, _, _, _, _ = row
        if img_name in val_list:
            img_path = '{}/{}'.format(val_path, img_name)
            if not os.path.exists(img_path):
                print(img_name, 'nahi mili val mein')
                continue
            row[0] = img_path
            val_annot_list.append(row)

        else:
            if img_name == "'.jpg":
                img_name = '0.jpg'
            img_path = '{}/{}'.format(train_path, img_name)
            if not os.path.exists(img_path):
                print(img_name, 'nahi mili train mein')
                continue
            row[0] = img_path
            train_annot_list.append(row)

with open('train_annot.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(train_annot_list)

with open('validn_annot.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(val_annot_list)
