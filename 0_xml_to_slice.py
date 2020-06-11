"generates slices out of each annotation in a custom object detection dataset"

"VOC format must contain an xml file for each image, with all the categories in a single ElementTree, with each bounding box labelled with its x1,y1,x2,y2 cordinates"

"xml file for each image returned by labelImg is in this format:"

"put all the images in a folder named train "
"put all the xmls in a folder named xmls "
"""
<annotation>
	<folder>Pictures</folder>
	<filename>13072751_1029937800387044_4957010403805370308_o.jpg</filename>
	<path>C:/Users/asus/Pictures/13072751_1029937800387044_4957010403805370308_o.jpg</path>
	<source>
		<database>Unknown</database>
	</source>
	<size>
		<width>2048</width>
		<height>1365</height>
		<depth>3</depth>
	</size>
	<segmented>0</segmented>
	<object>
		<name>person</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>840</xmin>
			<ymin>785</ymin>
			<xmax>991</xmax>
			<ymax>1133</ymax>
		</bndbox>
	</object>
	<object>
		<name>person2</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>986</xmin>
			<ymin>725</ymin>
			<xmax>1138</xmax>
			<ymax>1126</ymax>
		</bndbox>
	</object>
</annotation>
"""
"txt file saved at the end, will have a line by line list of details of individual bounding boxes in all images, in the format:"
"image_file_name.extension, x1_cordinate, y1_cordinate, x2_cordinate, y2_cordinate, object_class"

import os
import xml.etree.ElementTree as ET
from tqdm import tqdm
import cv2

categories = []
cat_count = {}

tagged_data = []
path = 'xmls'
images_fold = 'train'
slices_main_fold = 'slices'

if not os.path.exists(slices_main_fold):
	os.makedirs(slices_main_fold)

loosen_slice = True
	
xmls = [file for file in os.listdir(path) if file.endswith(('.xml'))]
print(len(xmls))
for file in tqdm(xmls):
    xml_path = os.path.join(path, file)
    tree = ET.parse(xml_path)
    root = tree.getroot()
    file_name = root[1].text  # filename
    img = cv2.imread(os.path.join(images_fold,file[:-3]+'jpg'))
    le,br = img.shape[:2]
    for child in root:
        if child.tag == 'object':
            category = child[0].text
            if not category in categories:
            	cat_path = os.path.join(slices_main_fold,category)
            	if not os.path.exists(cat_path):
            		os.makedirs(cat_path)
            cordinates = [int(k.text) for k in child[4]]
            x1, y1, x2, y2 = cordinates
            if not loosen_slice:
            	slicy = img[y1:y2,x1:x2]
            	cv2.imwrite(os.path.join(slices_main_fold,category,'{}@{}@{}@{}@{}.jpg'.format(file[:-4],x1,y1,x2,y2)),slicy)
            else:
            	cv2.rectangle(img,(x1,y1),(x2,y2),(255,255,255),2)
            	x1_ = x1-int(0.5*(x2-x1)) if x1-int(0.5*(x2-x1)) > 0 else 0
            	x2_ = x2+int(0.5*(x2-x1)) if x2+int(0.5*(x2-x1)) < br else br
            	y1_ = y1-int(0.5*(y2-y1)) if y1-int(0.5*(y2-y1)) > 0 else 0
            	y2_ = y2+int(0.5*(y2-y1)) if y2+int(0.5*(y2-y1)) < le else le
            	slicy = img[y1_:y2_,x1_:x2_]
            	cv2.imwrite(os.path.join(slices_main_fold,category,'{}@{}@{}@{}@{}.jpg'.format(file[:-4],x1,y1,x2,y2)),slicy)