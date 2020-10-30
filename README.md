# Description

Post labelling object detection data, labelling verification by separately class-wise saving all annotation slices for more accurate rechecking; then stratifically splitting the whole dataset into train and val sets ensuring relatively equal distribution of all object classes in the resultant sets.

These set of scripts can be used to verify custom object detection annotations and then split the whole dataset into train and validation stratifically. That implies the total number of occurences of each class in validation data shall be proportional to the their occurences in training data.

____________________________________________________________________________________________________________

It expects input as a set of images and their annotations in PASCAL VOC format as xml files.

The process of verification of annotation is done by:

a. Extracting slices of each annotation and saving it as an image in a separate folder for that class.

b. Then those folders of individual classes can be manually checked, and any incorrectly labeled annotation's slice can be then moved to the correct class's folder.

c. Then a script will scan the folder with corrected slices in it and generate a csv file containing the correct annotation info.

This would be possible, because each slice's image name contains the information of the root image from which it was extracted and it's  location (x1,y1,x2,y2) in the root image.

The csv thus generated thus contains the entire annotation information of the custom dataset.

The csv is then used to generate a dictionary containing the information of number of occurences of each class in each image.

To generate a stratified validation data:

a. Beginning from the most rare class moving towards the most frequent one, adeqaute number of images are seperated which in totatlity comprise adequate number of validation annots of that class i.e. atleast a certain percentage of the total instances of that class in the dSet.

b. From there, for each succesive class, images of that class are being added to validation dataset, such that that class's adequate number of instances are included in the val dataset.
