# Scripts for merging files and PDF documents


The [file_merger.py](https://github.com/ilalouch/scripts/blob/master/file_merger.py) script was written for a project - it merges files based on words in the 1st column. 

Some words in the old file have a description, others don't. All the words in the new file have a description.
By comparing the 2 files, the script does the following things: 
1. if a word is present only in the old file, then it is only copied and added to the final merged file; 
2. if a word exists in both files but with different descriptions, the new description is appended to the old one in the final merged file;
3. if a word is in the new file, but not in the old one, then it is appended to the final merged file;

The [pdf_merger.py](https://github.com/ilalouch/scripts/blob/master/pdf_merger.py) script merges 3 PDF files into a single document. 
