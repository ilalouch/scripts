#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# program that combines three pdf files into a single one using PyPDF2

import PyPDF2

# open the pdf files for combining
pdfFile1 = open('file1.pdf', 'rb')
pdfFile2 = open('file2.pdf', 'rb')
pdfFile3 = open('file3.pdf', 'rb')

# read pdf contents
reader1 = PyPDF2.PdfFileReader(pdfFile1)
reader2 = PyPDF2.PdfFileReader(pdfFile2)
reader3 = PyPDF2.PdfFileReader(pdfFile3)

# to write combined file into a new file
writer = PyPDF2.PdfFileWriter()

# iterate over the pages in every pdf file and add them into the final document
for pagNum in range(reader1.numPages):
    page = reader1.getPage(pagNum)
    writer.addPage(page)

for pagNum in range(reader2.numPages):
    page = reader2.getPage(pagNum)
    writer.addPage(page)

for pagNum in range(reader3.numPages):
    page = reader3.getPage(pagNum)
    writer.addPage(page)

# output the merged pdf into the working directory
combinedPdf = open('combinedpdf.pdf', 'wb')
writer.write(output)
output.close()

# close files
pdfFile1.close()
pdfFile2.close()
pdfFile3.close()
