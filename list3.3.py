import PyPDF2
import sys

final = PyPDF2.PdfWriter()
files = sys.argv 
files.pop(0)
for file in files:
    input = PyPDF2.PdfReader(file)
    for page_num in range(input.numPages):
        page = input.getPage(page_num)
        final.addPage(page)

output = open('merged' + files[0], 'wb')
final.write(output)