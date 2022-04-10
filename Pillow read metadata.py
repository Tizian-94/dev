import csv
from PIL import Image
from PIL.ExifTags import TAGS

my_img = Image.open("267770660.jpg")

exif_data = my_img.getexif()

for tagId in exif_data:
    tag = TAGS.get(tagId, tagId)
    data = exif_data.get(tagId)

    print(f"{tag:5}: {data}")

datasum = (f"{tag}: {data}")
data_count = 0

with open('output.csv', 'w', newline='') as csvfile:
    csv_reader = csv.DictReader(csvfile)

    fieldnames = ['YResolution', 'XResolution', 'Datetime']

    csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=',')

    csv_writer.writeheader()

for line in csvfile:
    data_count += 1
    csv_writer.writerow(datasum)
    

    #for line in csv_reader:
        #print(line)

    #with open('new_eggs.csv', 'w') as new_file:
        #fieldnames = ['YResolution', 'XResolution', 'Datetime']
        
       #csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

       # csv_writer.writeheader()

    #for line in csv_reader:
       # csv_writer.writerow(f"{tag:5}: {data}")