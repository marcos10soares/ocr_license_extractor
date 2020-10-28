#!/usr/local/bin/python3

import sys
import subprocess
import pytesseract
from os import listdir
from progress.bar import Bar
from PIL import Image, ImageOps
from os.path import isdir, isfile, join

def get_files_in_directory(path_to_files):
    onlyfiles = [f for f in listdir(path_to_files) if isfile(join(path_to_files, f))]
    onlyfiles.sort()
    return onlyfiles

def crop_license(pil_img):
    return pil_img.crop((100,460, 640,500))

def parse_license(files, path_to_files):
    licenses = []
    string_number = ''
    bar = Bar('Extracting licenses', max=len(files))
    for image in files:
        img = Image.open(path_to_files + image)        
        img = crop_license(img)
        license_number = pytesseract.image_to_string(img,  lang='eng')
        license_number = license_number.strip()
        license_number = license_number.replace(" ", "")
        licenses.append(license_number)
        string_number += license_number
        bar.next()
    bar.finish()
    print("Licenses extracted to file licences_ocr.txt")
    return licenses

def write_file(licenses):
    file1 = open("licenses_ocr.txt", "w")  
    for this_license in licenses:
        file1.write(this_license + "\n")
    file1.close()

def main():
    files = get_files_in_directory('./img/')
    licenses = parse_license(files, './img/')
    write_file(licenses)

if __name__ == "__main__":
    main()
