import csv
import os
from PIL import Image
from PIL.ExifTags import TAGS
import PIL.Image
from pathlib import Path

scan = Image.open("267770660.jpg")

#image_path = "\\Users\\tizia\\Dev"

#jpg_file = {}

exif_data = scan.getexif()

for tagId in exif_data:
    tag = TAGS.get(tagId, tagId)
    data = exif_data.get(tagId)

#for n, file in enumerate(os.listdir(image_path)):
    #if file[-3:] == 'JPG' :
        #parts = str(file).split('-')
        #jpg_file.update({parts[len(parts)-1]:file})

#scan_object = Scan.objects.get(code=scan)

with open('metadata_scrape.csv', 'w', encoding='utf-8-sig') as new_file:
    csv_data = csv.DictReader(new_file, delimiter=',')

    fieldnames = ['YResolution', 'XResolution', 'Datetime']

    csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter = '\t')

    csv_writer.writeheader()
        
try:
    img = PIL.Image.open(image_path + jpg_file['filename'])
    print('file opened')
    exif_data = piexif.load(image_path + jpg_file['filename'])
    print('exif data retrieved')
except:
    print('file not found', 'filename')

with open('metadata_scrape.csv', 'r') as f:
    csv_reader = csv.DictReader(csv_file)


for line in csv_reader:
    csv_writer.writerow(line)