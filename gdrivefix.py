import os
import sys
from xml.dom import minidom
import shutil

#ebooks_directory = "/home/mendhak/Desktop/EBooks"
ebooks_directory = raw_input("Enter path to your ebooks directory: ")

print ebooks_directory
if ebooks_directory is None or len(ebooks_directory) < 3:
    print "Please enter a proper directory path"
    exit(1)



def getCalibreId(opfPath):
    xmldoc = minidom.parse(opfPath)
    itemlist = xmldoc.getElementsByTagName('dc:identifier')
    for identifier in itemlist:
        if 'id' in identifier.attributes.keys() and identifier.attributes['id'].value == 'calibre_id':
            return identifier.childNodes[0].data

for root, dirs, files in os.walk(ebooks_directory):
    for file in files:
        if file.endswith('metadata.opf'):
            calibre_id = getCalibreId(os.path.join(root, file))
            calibre_fragment = " (" + calibre_id + ")"
            if calibre_fragment not in root:
                print "Moving files to " + os.path.join(root + calibre_fragment)
                shutil.rmtree(os.path.join(root+calibre_fragment), ignore_errors=True)
                shutil.move(os.path.join(root), os.path.join(root+calibre_fragment))




