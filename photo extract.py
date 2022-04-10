import pyexiv2
import os
import csv

print("Enter the full path to the directory that your images are conatined in.")
print ("-------------------------------------------")
newFileObj = open('C:\\users\\wilson\\desktop\\Metadata.csv', 'w')
with open(newFileObj, 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter='',
    quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Beans'])
    spamwriter.writerow(['Spam', 'Loverly Spam', 'Wonderful Spam'])

targ_files = os.listdir(targ_dir)

def getEXIFdata (imageFile):
    if imageFile.endswith(".db"):
        f = 1
    else:

        EXIFData = pyexiv2.ImageMetadata(imageFile)
        EXIFData.read()
        CamMake = EXIFData['Exif.Image.Make']
        DateTime = EXIFData['Exif.Image.DateTime']
        CamModel = EXIFData['Exif.Image.Model']
    for image in targ_files:
        getEXIFdata(targ_dir+"\\"+img)
        newFileObj.write(DateTime+' , '+CamMake+' , '+CamModel+'\r\n')
newFileObj.close()

end = raw_input("Press Enter to Finish: ")
