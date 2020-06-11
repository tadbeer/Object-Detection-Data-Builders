import pickle
import numpy as np

# picks the validation data from a unified single database of images with annotations.
# Beginning from the most rare class moving towards the most frequent one,
# adeqaute number of images are seperated which in totatlity comprise adequate number of validation annots of that class
# i.e. atleast a certain percentage of the total instances of that class in the dSet.
# From there, for each succesive class, images of that class are being added to validation dSet,
# such that that class's adequate number of instances are included in the val dSet.

val_ratio = 0.17

# uploading the image and annotation dictionary
with open('annot_freq.pickle', 'rb') as file:
    imdict = pickle.load(file)

# building the dictionary comprising the number of occurences of each class in the dSet
# also builds a dictionary of 0s put against each class, for keeping count of each class currently in validation set.
class_dict = {}
val_freq_dict = {}
for img in imdict:
    for klass in imdict[img]:
        if not klass in class_dict:
            class_dict[klass] = 0
            val_freq_dict[klass] = 0
        class_dict[klass] += imdict[img][klass]

# a list of frequencies of all class in the ascending order, vali is hindi waala 'vali' for 'list'.
vali = [class_dict[i] for i in class_dict]
vali.sort()


def classy_images(klass, val_ims):

    # returns a list of all the images containing a particluar class, which are not already part of val dSet

    #print('Processing classy images for', klass)
    classy_imgs = []
    for img in imdict:
        if klass in imdict[img] and not img in val_ims:
            classy_imgs.append(img)

    return(classy_imgs)


val_ims = []  # array to append validation images to

for freq in vali:  # moving iteratively in ascending order of class frequencies
    for klass in class_dict:
        if class_dict[klass] == freq:
            classy_imgs = classy_images(klass, val_ims)
            val_freq_desrd = int(val_ratio * freq)  # .17 is the desired ratio of val to total
            val_freq_curnt = val_freq_dict[klass]  # assigning the current value of class instances in validation dSet
            indexes_done = []  # a list for storing the random indexes that have been already used
            while val_freq_curnt < val_freq_desrd:
                index = np.random.randint(len(classy_imgs))  # random index position for picking random image from all images containing a particular class
                if index in indexes_done:
                    continue
                indexes_done.append(index)
                val_freq_curnt += imdict[classy_imgs[index]][klass]
                for klass_for_val in imdict[classy_imgs[index]]:  # adding all the instances of the rest of classes, going in the val dSet
                    val_freq_dict[klass_for_val] += imdict[classy_imgs[index]][klass_for_val]
                val_ims.append(classy_imgs[index])

# printing the ocuurence of each class in total dSet and the val dSet
ratios = 0
total_items = 0
for item in vali:
    for klass in class_dict:
        if class_dict[klass] == item:
            ratio = val_freq_dict[klass] / item
            ratios += item * ratio
            total_items += item
            print(klass, item, val_freq_dict[klass], val_freq_dict[klass] / item)

total_val_items = sum([val_freq_dict[i] for i in val_freq_dict])
abs_ratio = total_val_items / total_items
print(abs_ratio)

with open('val_abs_{:.3f}.txt'.format(abs_ratio), 'w') as file:
    for line in val_ims:
        file.write(line + '\n')
