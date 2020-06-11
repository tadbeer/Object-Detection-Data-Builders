import csv
import pickle

# creates a 'classes.csv containing a list of classes with indexes assigned to each ;  used in fizyr/keras-retinanet'

# creates a dictionary containing the same information, usable while running predictions to 
# know if what is the class name of a particular class index

root_ims_csv_path = 'annotation.csv'
classes = []
class_list_dict = {}

with open(root_ims_csv_path, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        _, _, _, _, _, klass = row
        if not klass in classes:
            classes.append(klass)

classes.sort()
for i, klass in enumerate(classes):
    classes[i] = [klass, i]
    class_list_dict[i] = klass


#write csv for class list
with open('classes.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(classes)

# write dictionary for class list, for later use in predict script
with open('class_list_dict.pickle', 'wb') as file:
    pickle.dump(class_list_dict, file, protocol=pickle.HIGHEST_PROTOCOL)
