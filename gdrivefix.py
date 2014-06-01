import os
from xml.dom import minidom

ebooks_directory = "/home/mendhak/Desktop/EBooks"


def getCalibreId(opfPath):
    xmldoc = minidom.parse(opfPath)
    itemlist = xmldoc.getElementsByTagName('dc:identifier')
    for identifier in itemlist:
        if 'id' in identifier.attributes.keys() and identifier.attributes['id'].value == 'calibre_id':
            return identifier.childNodes[0].data

for root, dirs, files in os.walk(ebooks_directory):
    for file in files:
        if file.endswith('metadata.opf'):
            print os.path.join(root, file)
            print getCalibreId(os.path.join(root, file))



