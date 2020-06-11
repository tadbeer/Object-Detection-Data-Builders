import pickle

#checks the dictionary saved for the frequency of classes.

with open('annot_freq.pickle', 'rb') as file:
    dicty = pickle.load(file)

class_dict = {}
c = 0
for img in dicty:
    for klass in dicty[img]:
        
        if not klass in class_dict:
            class_dict[klass] = 0
        class_dict[klass] += dicty[img][klass]

#'vali' stands for 'list' in hindi viz shabdavali, deepawali,
vali = [class_dict[i] for i in class_dict]
vali.sort()
for item in vali:
    for klass in class_dict:
        if class_dict[klass] == item:
            print(klass, item)