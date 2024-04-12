from PyPDF2 import PdfWriter, PdfReader
from sys import argv
from os import path, access, R_OK
"""
Traderas fraktsedlar kommer i PDF-format och innehåller en massa onödigt innehåll,
vilket gör att det inte går att skriva ut (A4) på en etikettskrivare (4x6 inch).
Detta script tar en PDF-fil som argument och skapar en ny PDF-fil med etiketten i rätt storlek.

Author : Jonas Björk <jonas.bjork@gmail.com>
Date   : 2024-04-12
Version: 1.0

Usage:
$ python traderacrop.py <pdf file>

Example:
$ python traderacrop.py frakt.pdf
File cropped_frakt.pdf created

"""

if len(argv) != 2:
    print('Usage:\n traderacrop.py <pdf file>')
    exit(1)

filename = argv[1]
if not (path.isfile(filename) and access(filename, R_OK)):
    print(f'File {filename} not found or not readable')
    exit(1)

reader = PdfReader(filename) 
writer = PdfWriter()

# Cropbox was calculated with help from https://stackoverflow.com/questions/457207/cropping-pages-of-a-pdf-file/68245426#68245426
# using the calculator at https://jsfiddle.net/p9L6rsco/
for page in reader.pages:
  page.cropbox.upper_left = (13,708)
  page.cropbox.lower_right = (285,201)
  writer.add_page(page)

try:
  newfilename = 'cropped_' + path.basename(filename)
  with open(newfilename,'wb') as fp:
    writer.write(fp)
    print(f'File {newfilename} created')
    writer.close()
except Exception as e:
   print(f'Error: {e}')

