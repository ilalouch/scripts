#! /usr/bin/env python
#! /usr/bin/python
# -*- coding: utf-8 -*-


"""
"""

import codecs


old_tocs = codecs.open("old_file.txt", encoding='utf-8')
new_tocs = codecs.open("new_file.txt", encoding='utf-8')


old_dict={}
for line in old_toc:
    value = ""
    if ':' in line: 
	toc = line.split(":")[0].strip()
	value = line.split(":")[1]
    else: toc = line.strip()
    old_dict[toc] = value


for lines in new_toks:
    new_toc = lines.split(":")[0].strip()
    new_value =  lines.split(":")[1].strip() 
    if "," in new_value: 
        new = ""
        new = new_value.split("=")[1].strip()
        new_value = "keyw=["+ new+"]"
    old_toc = old_dict.get(new_toc.strip()) #keeps old information

    if old_toc != None:
	if 'keyw' in str(old_toc.encode('utf-8')): #adds new keyw next to the already existing ones
	    result = ""
	    for item in old_toc.split(' '):
		if 'keyw' in item: #adds new keyw next to the existing ones
		    new_keyw = item.split("keyw=")[1].split("'")[0]
            	    if " " in new_keyw: new_keyw = new_keyw.split(' ')[0]
		    result = result + " keyw=[" + lines.split("keyw=")[1].strip() + ',' + new_keyw.strip() + "]"
		else:
		    result = result + " " + item
	    old_dict[new_toc.strip()] = result

        else: #adds keyw to existing workds and keeps the values the words previously had
           old_dict[new_toc.strip()] = new_value + "" + old_dict[new_toc.strip()]

    else: #adds new words to the dict with feature
	old_dict[new_toc.strip()] = new_value +" feature" 
		
outToc = codecs.open("merge-result.txt", "w", encoding='utf-8') #write new words to file
for k,v in old_dict.items():
    print k,v
    if v: outToc.write (k +  "\t: " + v + "\n")
    else: outToc.write (k + "\n")

outToc = codecs.open("merge-result.txt", "r", encoding='utf-8')
outToc1 = codecs.open("result_nospace.txt", "w", encoding='utf-8') #remove empty lines

for line in outToc:
    if not line.strip(): continue
    print line
    outToc1.write(line)

outToc.close()
outToc1.close()
