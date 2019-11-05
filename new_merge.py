#! /usr/bin/env python
#! /usr/bin/python
# -*- coding: utf-8 -*-


"""
"""

import codecs


old_toks = codecs.open("tokens.txt", encoding='utf-8')
new_toks = codecs.open("toks_morpar_nouns.txt", encoding='utf-8')


old_dict={}
for line in old_toks:
    value = ""
    if '::' in line: 
	tok = line.split("::")[0].strip()
	value = line.split("::")[1]
    else: tok = line.strip()
    old_dict[tok] = value


for lines in new_toks:
    new_tok = lines.split("::")[0].strip()
    new_value =  lines.split("::")[1].strip() 
    if "," in new_value: 
        new = ""
        new = new_value.split("=")[1].strip()
        new_value = "morpar=["+ new+"]"
    old_tok = old_dict.get(new_tok.strip()) #keeps old information

    if old_tok != None:
	if 'morpar' in str(old_tok.encode('utf-8')): #adds new morpars next to the already existing ones
	    result = ""
	    for item in old_tok.split(' '):
		if 'morpar' in item: #adds new morpars next to the existing ones
		    new_morpar = item.split("morpar=")[1].split("'")[0]
            	    if " " in new_morpar: new_morpar = new_morpar.split(' ')[0]
		    result = result + " morpar=[" + lines.split("morpar=")[1].strip() + ',' + new_morpar.strip() + "]"
		else:
		    result = result + " " + item
	    old_dict[new_tok.strip()] = result

        else: #adds morpar to existing tokens and keeps the values the tokens previously had
           old_dict[new_tok.strip()] = new_value + "" + old_dict[new_tok.strip()]

    else: #adds new tokens to the lexicon with prons=auto
	old_dict[new_tok.strip()] = new_value +" prons=auto" 
		
outTok = codecs.open("tokens-result.txt", "w", encoding='utf-8') #write new tokens to file
for k,v in old_dict.items():
    print k,v
    if v: outTok.write (k +  "\t:: " + v + "\n")
    else: outTok.write (k + "\n")

outTok = codecs.open("tokens-result.txt", "r", encoding='utf-8')
outTok1 = codecs.open("tokens_nospace.txt", "w", encoding='utf-8') #remove empty lines

for line in outTok:
    if not line.strip(): continue
    print line
    outTok1.write(line)

outTok.close()
outTok1.close()
