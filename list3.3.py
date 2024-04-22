import PyPDF2
import sys

final = PyPDF2.PdfWriter()
for file in sys.argv:
    input = PyPDF2.PdfReader(file)
    for page_num in range(input.numPages):
        page = input.getPage(page_num)
        final.addPage(page)

output = open('merged' + sys.avg[0], 'w')
final.write(output)