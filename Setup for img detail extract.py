#Setup for img detail extract
#setup needed to run like in Django - to read and save from db
#------------------------------------------------------------------------------------------
import sys
import os
import django
import csv

wd = os.getcwd()
wd = wd + '\\'
#print(wd)
sys.path.append(wd)
os.environ['DJANGO_SETTINGS_MODULE'] = 'tools.settings'
django.setup()
#------------------------------------------------------------------------------------------

import PIL.Image
import piexif
from map.models import Image, Camp
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
from io import BytesIO #required for reduce file size save

import uuid
from django.conf import settings
from pathlib import Path

print('django setup complete')
print('\n' + '#'*50 + '\n      ##### 360 Photo Processing Script #####\n' + '#'*50 + '\n')

#############################################################
############# specify folder to be processed ##################

folder= "fgo"

#############################################################
#############################################################


# folder specifications

folder_path = "\\\\Users\\tizia\\testfiles\\file\\" + folder + "\\"
image_path = folder_path + "\\publish\\"


# get all image file names for each processing
jpg_file = {}

for n, file in enumerate(os.listdir(image_path)):
    if file[-3:] == 'JPG':
        parts = str(file).split('-')
        print(len(parts))
        jpg_file.update({parts[len(parts)-1]:file})
        print(jpg_file)

#folder_object = Folder.objects.get(code=folder)#
#with open(folder_path + folder + 'eggs.csv', 'r',encoding='utf-8-sig') as csv_file:#
#csv_data = csv.DictReader(csv_file, delimiter=',')#


