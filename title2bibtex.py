#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 20:43:05 2023

@author: ckettmayer
"""
### Fetch bibtex data from article titles using CrossRef ###

import habanero 
import re


titles = [['Quasi-Two-Dimensional Kolmogorov Flow: Bifurcations and Exact Coherent Structures'],
          ['Two-Dimensional Turbulence'],
          ['Two dimensional turbulence: a physicist approach']]

# create CrossRef client
cr = habanero.Crossref()

# retrieve DOI from titles
dois = []
for i in titles:
    # look for article
    query = i
    results = cr.works(query=query)
    
    # retrieve first result and DOI if avalaible
    if results['status'] == 'ok' and results['message']['items']:
        article = results['message']['items'][0]
        doi = article.get('DOI')
        if doi:
            dois.append(doi)
            # print("DOI:", doi)
        else:
            dois.append('doi not found')
            # print("No se encontró el DOI.")
    else:
        dois.append('crossref results not found')
        # print("No se encontraron resultados en CrossRef.")    
     
    
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
    
    