# OCR License Extractor

OCR License Extractor is a short python script that I wrote for a CTF(syskronCTF) where I needed to get a list of all the licenses written on images.

## Installation

Make sure you have python3 installed and run:

```bash
python3 -m pip install -r requirements.txt
```

## Usage

The folder to read the images from is hardcoded so just open the script and change line 43, the variable named folder_to_read_the_images_from.

Output file is also hardcode, so if you would like to change that just change line 46.

```python
def main():
    folder_to_read_the_images_from = './img/' # change this to the images folder
    files = get_files_in_directory(folder_to_read_the_images_from)
    licenses = parse_license(files, folder_to_read_the_images_from)
    write_file(licenses, 'licenses_ocr.txt')  # change this for the output file

```

Then just run the command:
```bash
python3 license_extractor.py
```

## Example

![Example](https://github.com/marcos10soares/ocr_license_extractor/raw/master/yKLbXzLJ7H.gif)

## License
[MIT](https://choosealicense.com/licenses/mit/)