import os
import glob
import xml.etree.ElementTree as ET

def get_annotation_summary(annotations_folder):
    training_xmls = glob.glob(annotations_folder + '/*.xml')
    print('There are', len(training_xmls), 
        '.xml annotation files in the given folder.')

    animal_count = {}

    for xml in training_xmls:
        tree = ET.parse(xml)
        root = tree.getroot()

        #Get number of frames in the annotated sequence
        for animal in root.findall('object'):
            name = animal.find('name').text
    #         name = name.split('_')
    #         animal_name = name[0]
            animal_name = name
            if animal_name in animal_count:
                animal_count[animal_name] += 1
            else:
                animal_count[animal_name] = 1

    print(animal_count)
    return(animal_count)


