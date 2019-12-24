# Scripts for merging files and PDF documents


First script was written for a project - it merges files based on words in the 1st column. 
Explanation: 
    Some items in the old file have a description, others don't. All the items in the new file have a description.
    By comparing the 2 files, the script does the following things: 
           1. if an item is present only in the old file, then the item is only added to the merged file; 
           2. if an item is in both files but with different descriptions, the new description is aded to the old one;
           3. if an item is in the new file, but not in the old one, then it is appended to the merged file;

Second script merges 3 PDF files into a single document. 
