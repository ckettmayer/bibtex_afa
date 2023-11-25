#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 12:35:25 2023

@author: ckettmayer
"""
### Fetch bibtex data from doi using CrossRef ###

import habanero 
import re


dois = [[''],
          ['10.1146/annurev-fluid-120710-101240'],
          ['https://doi.org/10.1016/S0370-1573(01)00064-3'],
          [''],
          [],
          [],
          [],
          [],
          [],
          [],
          []]

     
    
# retrieve bibtex data from DOI
bibtex = []
for j in dois:
     article_info = habanero.cn.content_negotiation(j)
     # add line breaks
     text = article_info
     text_n = text.replace(',', ',\n')
     # delet month, url and ISSN info
     text_clean = re.sub(r'^\s*url\s*=.*$', '', text_n, flags=re.MULTILINE)
     text_clean = re.sub(r'^\s*month\s*=.*$', '', text_clean, flags=re.MULTILINE)
     text_clean = re.sub(r'^\s*ISSN\s*=.*$', '', text_clean, flags=re.MULTILINE)
     # delet empty lines
     text_clean = "\n".join(line for line in text_clean.splitlines() if line.strip())
    
     bibtex.append(text_clean)


# print bibtex for all ref
for k in range(len(bibtex)):
    print(f'% ref {k+1}  \n {bibtex[k]} \n')        
    