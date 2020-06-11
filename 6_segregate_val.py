import os
import shutil

#makes a separate folder for validation images, picked as per the list created in earlier step

#put the name of the 'txt' file generated in the previous step as 'val_list_path'

val_list_path = 'val_abs_0.196.txt'
root_ims_folder_path = 'train'
val_folder_path = 'validn'

if not os.path.exists(val_folder_path):
    os.mkdir(val_folder_path)

val_list = []

with open(val_list_path, 'r') as file:
    for line in file:
        val_list.append(line[:-1])

for image in val_list:
    src_path = os.path.join(root_ims_folder_path, image)
    if not os.path.exists(src_path):
        print(image, 'nahin mili')
        continue
    dst_path = os.path.join(val_folder_path, image)
    shutil.move(src_path, dst_path)
