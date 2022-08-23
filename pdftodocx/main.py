## Importing dependencies
from pdf2docx import Converter

## defining input and output paths

pdf_file = 'A SIMPLE SAMPLE PDF.pdf'
docx_file = 'A SIMPLE SAMPLE PDF.docx'

##Converting pdf file to WORD (DOCX)

cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()

