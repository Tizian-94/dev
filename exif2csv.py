import sys
import csv
import os
import argparse
import pyexiv2

def main():
    parser = argparse.ArgumentParser(description="Change the txt file to csv.")
    parser.add_argument("-i", action="store", dest="infile")
    parser.add_argument("-o", action="store", dest="outfile")
    parser_argument = parser.parse_args()

    fatherdir = os.getcwd()  # code directory
    inputfile = outputfile = None

    # input exif file
    if parser_argument.infile:
        infilepaths = os.path.split(parser_argument.infile)
        # 'C:\User\lenovo\Desktop\pakistan.txt' ---> ['C:\User\lenovo\Desktop','pakistan.txt']
        if infilepaths[0]:  # full path
            inputfile = parser_argument.infile
            fatherdir = infilepaths[0]
        # 'pakistan.txt' ---> ['','pakistan.txt']
        else:  # only file name
            inputfile = fatherdir + '/' + parser_argument.infile
    # output csv file
    if parser_argument.outfile:
        outfilepaths = os.path.split(parser_argument.outfile)
        if outfilepaths[0]:  # full path
            outputfile = parser_argument.outfile
        else:
            outputfile = fatherdir + '/' + parser_argument.outfile
    else:
        outputfile = fatherdir + '/test_csv.csv'
    parse(inputfile, outputfile)


def parse(inputfile, outputfile):
    csvcontent = file(outputfile, 'wb')
    writer = csv.writer(csvcontent)

    exif_data = getEXIFdata(inputfile)
    writer.writerow([exif_data['Exif.Image.Orientation'].value,
                     exif_data['Exif.Photo.PixelXDimension'].value,
                     exif_data['Exif.Photo.PixelYDimension'].value])
    # for line in open(inputfile).readlines():
    #     writer.writerow([a for a in line.split('\t')])

    csvcontent.close()

def getEXIFdata (imageFile):
    if imageFile.endswith(".db"):
        print('Skip this file')
    else:
        exif_data = pyexiv2.ImageMetadata(imageFile)
        exif_data.read()
        for s, v in exif_data.items():
            print(s, v)
        cam_a = exif_data['Exif.Image.Orientation'].value
        cam_b = exif_data['Exif.Photo.PixelXDimension'].value
        cam_c = exif_data['Exif.Photo.PixelYDimension'].value
        # add exif value
        ekey = 'Exif.Photo.UserComment'
        evalue = 'A comment.'
        exif_data[ekey] = pyexiv2.ExifTag(ekey, evalue)
        #metadata.write()
        return exif_data

if __name__ == '__main__':
    main()