import os
import PyPDF2

# Mean Girls parsing

# Tutorial from: https://ironpdf.com/blog/pdf-tools/how-to-convert-pdf-to-text-python/
# Changed some lines for updated documentation

# create a pdf file object
filename = 'movies/scripts/mean_girls/mg_ds.pdf'
filename = 'test.pdf'
pdfFileObj = open(filename, 'rb')
# create a pdf reader object
pdfReader = PyPDF2.PdfReader(pdfFileObj)
# print number of pages in the pdf file
print("Page Number:", len(pdfReader.pages))
# create a page object
pageObj = pdfReader.pages[0]
# extract text from page
text = pageObj.extract_text()
# display just the text
print(text)

print('here')
# for i in range(len(pdfReader.pages)):
#     print( pdfReader.pages[i].extract_text())

#Doesn't work