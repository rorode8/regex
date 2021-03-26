#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/rorode8/regex/blob/main/regex.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# In[1]:


import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import six



# In[ ]:





# In[ ]:





# 

# código para probar rápido, detecta todas las declaraciones de ints excepto los arreglos con `[]` se puede probar aqui https://regex101.com/r/DVGAfu/1 (version 2: https://regex101.com/r/wOoMH0/2 , https://regex101.com/r/wOoMH0/3) 
# 
# para doubles|floats: https://regex101.com/r/R2z3VB/1 (version 2: https://regex101.com/r/K1CLoe/1 , https://regex101.com/r/K1CLoe/2)
# 
# 
# para String: https://regex101.com/r/DeNIC1/1 (version 2: https://regex101.com/r/DeNIC1/2 , https://regex101.com/r/DeNIC1/3)
# 
# chars: https://regex101.com/r/Lwq9eH/1 (version 2: https://regex101.com/r/v9rdXR/1)
# 
# booleans: https://regex101.com/r/onqgVh/1 (version 2: https://regex101.com/r/zWB3QX/2)
# 
# byte: https://regex101.com/r/a8ThzX/1 (version 2: https://regex101.com/r/7NpfxU/1)
# 
# 
# object: https://regex101.com/r/OnLnUP/1
# 
# objetos con parametros https://regex101.com/r/nPeUMh/1 version 2: https://regex101.com/r/2fbNNE/1

# In[14]:






text = file = open("input.txt").read()


purge = re.compile(r'(\/\/.*$|(\/\*)(\w|\s|\*[^\/])*(\*\/))',re.MULTILINE) #elimina comentarios
text = purge.sub('',text)

print('TEXTO FUENTE-----------------------------------------------------------')
print(text)
print('------------------------------------------------------------------------')
print('')

d = {}
variables = {}

Pstring = r'\s+(\[\s*\]\s*\w+\s*(,\s*\w+|=(\s*(new\s+\1\s*\[\s*[1-9]\d*\s*\])|\s*{\s*\"[^"]*\"\s*(\s*,\s*\"[^"]*\"\s*)*}))?\s*(,\s*\w+\s*(\[\s*\])?\s*(=(\s*(new\s+\1\s*\[\s*[1-9]\d*\s*\])|\s*{\s*\"[^"]*\"\s*(\s*,\s*\"[^"]*\"\s*)*}))?)*|\w+\s*(,\s*\w+|=(\s*(new\s+\1\s*\[\s*[1-9]\d*\s*\])|\s*\"[^"]*\"\s*|\[\s*\]\s*(=\s*{\s*\"[^"]*\"\s*(\s*,\s*\"[^"]*\"\s*)*})?))?(,\s*\w+|,\s*\w+\s*=\s*\"[^"]*\"\s*|\s*\[\s*\]\s*(=(\s*(new\s+\1\s*\[\s*[1-9]\d*\s*\])|\s*{\s*\"[^"]*\"\s*(\s*,\s*\"[^"]*\"\s*)*}))?)*)\s*;'
Pchar = r"\s+(\[\s*\]\s*\w+\s*(,\s*\w+|=(\s*(new\s+\1\s*\[\s*[1-9]\d*\s*\])|\s*{\s*\'[^']\'\s*(\s*,\s*\'[^']\'\s*)*}))?\s*(,\s*\w+\s*(\[\s*\])?\s*(=(\s*(new\s+\1\s*\[\s*[1-9]\d*\s*\])|\s*{\s*\'[^']\'\s*(\s*,\s*\'[^']\'\s*)*}))?)*|\w+\s*(,\s*\w+|=\s*\'[^']\'\s*|\[\s*\]\s*(=(\s*(new\s+\1\s*\[\s*[1-9]\d*\s*\])|\s*{\s*\'[^']\'\s*(\s*,\s*\'[^']\'\s*)*}))?)?(,\s*\w+|,\s*\w+\s*=\s*\'[^']\'\s*|\s*\[\s*\]\s*(=(\s*(new\s+\1\s*\[\s*[1-9]\d*\s*\])|\s*{\s*\'[^']\'\s*(\s*,\s*\'[^']\'\s*)*}))?)*)\s;*"
Pint = r'\s+(\[\s*\]\s*\w+\s*(,\s*\w+|=(\s*{\s*\d+(\s*,\s*\d+\s*)*}|\s*(new\s+\1\s*\[\s*\d+\s*\])))?\s*(,\s*\w+\s*(\[\s*\])?\s*(=(\s*{\s*\d+(\s*,\s*\d+\s*)*}|\s*(new\s+\1\s*\[\s*\d+\s*\])))?)*|\w+\s*(,\s*\w+|=\s*\d+|\[\s*\]\s*(=(\s*(new\s+\1\s*\[\s*\d+\s*\])|\s*{\s*\d+(\s*,\s*\d+\s*)*}))?)?(,\s*\w+|,\s*\w+\s*=\s*\d+|\s*\[\s*\]\s*(=(\s*(new\s+\1\s*\[\s*\d+\s*\])|(\s*{\s*\d+(\s*,\s*\d+\s*)*})))?)*)\s*;'
Pdouble = r'\s+(\[\s*\]\s*\w+\s*(,\s*\w+|=(\s*(new\s+\1\s*\[\s*[1-9]\d*\s*\])|\s*{\s*[+-]?([0-9]*[.]?)[0-9]+(\s*,\s*[+-]?([0-9]*[.]?)[0-9]+\s*)*}))?\s*(,\s*\w+\s*(\[\s*\])?\s*(=(\s*(new\s+\1\s*\[\s*[1-9]\d*\s*\])|\s*{\s*[+-]?([0-9]*[.]?)[0-9]+(\s*,\s*[+-]?([0-9]*[.]?)[0-9]+\s*)*}))?)*|\w+\s*(,\s*\w+|=(\s*(new\s+\1\s*\[\s*[1-9]\d*\s*\])|\s*[+-]?([0-9]*[.]?)[0-9]+|\[\s*\]\s*(=\s*{\s*[+-]?([0-9]*[.]?)[0-9]+(\s*,\s*[+-]?([0-9]*[.]?)[0-9]+\s*)*})?))?(,\s*\w+|,\s*\w+\s*=\s*[+-]?([0-9]*[.]?)[0-9]+|\s*\[\s*\]\s*(=(\s*(new\s+\1\s*\[\s*[1-9]\d*\s*\])|\s*{\s*[+-]?([0-9]*[.]?)[0-9]+(\s*,\s*[+-]?([0-9]*[.]?)[0-9]+\s*)*}))?)*)\s*;'
Pboolean = r'\s+(\[\s*\]\s*\w+\s*(,\s*\w+|=(\s*(new\s+\1\s*\[\s*[1-9]\d*\s*\])|\s*{\s*(true|false)\s*(\s*,\s*(true|false)\s*)*}))?\s*(,\s*\w+\s*(\[\s*\])?\s*(=(\s*(new\s+\1\s*\[\s*[1-9]\d*\s*\])|\s*{\s*(true|false)\s*(\s*,\s*(true|false)\s*)*}))?)*|\w+\s*(,\s*\w+|=\s*(true|false)\s*|\[\s*\]\s*(=(\s*(new\s+\1\s*\[\s*[1-9]\d*\s*\])|\s*{\s*(true|false)\s*(\s*,\s*(true|false)\s*)*}))?)?(,\s*\w+|,\s*\w+\s*=\s*(true|false)\s*|\s*\[\s*\]\s*(=(\s*(new\s+\1\s*\[\s*[1-9]\d*\s*\])|\s*{\s*(true|false)\s*(\s*,\s*(true|false)\s*)*}))?)*)\s*;'
pbyte = r'\s+(\[\s*\]\s*\w+\s*(,\s*\w+|=(\s*(new\s+\1\s*\[\s*[1-9]\d*\s*\])|\s*{\s*(0b[01]{1,8}|0x[0-9a-fA-F]{1,2}|\d{1,3})\s*(\s*,\s*(0b[01]{1,8}|0x[0-9a-fA-F]{1,2}|\d{1,3})\s*)*}))?\s*(,\s*\w+\s*(\[\s*\])?\s*(=(\s*(new\s+\1\s*\[\s*[1-9]\d*\s*\])|\s*{\s*(0b[01]{1,8}|0x[0-9a-fA-F]{1,2}|\d{1,3})\s*(\s*,\s*(0b[01]{1,8}|0x[0-9a-fA-F]{1,2}|\d{1,3})\s*)*}))?)*|\w+\s*(,\s*\w+|=\s*(0b[01]{1,8}|0x[0-9a-fA-F]{1,2}|\d{1,3})\s*|\[\s*\]\s*(=(\s*(new\s+\1\s*\[\s*[1-9]\d*\s*\])|\s*{\s*(0b[01]{1,8}|0x[0-9a-fA-F]{1,2}|\d{1,3})\s*(\s*,\s*(0b[01]{1,8}|0x[0-9a-fA-F]{1,2}|\d{1,3})\s*)*}))?)?(,\s*\w+|,\s*\w+\s*=\s*(0b[01]{1,8}|0x[0-9a-fA-F]{1,2}|\d{1,3})\s*|\s*\[\s*\]\s*(=(\s*(new\s+\1\s*\[\s*[1-9]\d*\s*\])|\s*{\s*(0b[01]{1,8}|0x[0-9a-fA-F]{1,2}|\d{1,3})\s*(\s*,\s*(0b[01]{1,8}|0x[0-9a-fA-F]{1,2}|\d{1,3})\s*)*}))?)*)\s*;'
pObject = r'\s+(\[\s*\]\s*\w+\s*(,\s*\w+|=(\s*(new\s+\1\s*\[\s*[1-9]\d*\s*\])|\s*{\s*(new\s+\1\s*\(\s*([^,]?\w+[^,]?\s*(,\s*[^,]?\w+[^,]?)*)*\s*\)|(?!new\b)\w+)\s*(\s*,\s*(new\s+\1\s*\(\s*([^,]?\w+[^,]?\s*(,\s*[^,]?\w+[^,]?)*)*\s*\)|(?!new\b)\w+)\s*)*}))?\s*(,\s*\w+\s*(\[\s*\])?\s*(=(\s*(new\s+\1\s*\[\s*[1-9]\d*\s*\])|\s*{\s*(new\s+\1\s*\(\s*([^,]?\w+[^,]?\s*(,\s*[^,]?\w+[^,]?)*)*\s*\)|(?!new\b)\w+)\s*(\s*,\s*(new\s+\1\s*\(\s*([^,]?\w+[^,]?\s*(,\s*[^,]?\w+[^,]?)*)*\s*\)|(?!new\b)\w+)\s*)*}))?)*|\w+\s*(,\s*\w+|=\s*(new\s+\1\s*\(\s*([^,]?\w+[^,]?\s*(,\s*[^,]?\w+[^,]?)*)*\s*\)|(?!new\b)\w+)\s*|\[\s*\]\s*(=(\s*(new\s+\1\s*\[\s*[1-9]\d*\s*\])|\s*{\s*(new\s+\1\s*\(\s*([^,]?\w+[^,]?\s*(,\s*[^,]?\w+[^,]?)*)*\s*\)|(?!new\b)\w+)\s*(\s*,\s*(new\s+\1\s*\(\s*([^,]?\w+[^,]?\s*(,\s*[^,]?\w+[^,]?)*)*\s*\)|(?!new\b)\w+)\s*)*}))?)?(,\s*\w+|,\s*\w+\s*=\s*(new\s+\1\s*\(\s*([^,]?\w+[^,]?\s*(,\s*[^,]?\w+[^,]?)*)*\s*\)|(?!new\b)\w+)\s*|\s*\[\s*\]\s*(=(\s*(new\s+\1\s*\[\s*[1-9]\d*\s*\])|\s*{\s*(new\s+\1\s*\(\s*([^,]?\w+[^,]?\s*(,\s*[^,]?\w+[^,]?)*)*\s*\)|(?!new\b)\w+)\s*(\s*,\s*(new\s+\1\s*\(\s*([^,]?\w+[^,]?\s*(,\s*[^,]?\w+[^,]?)*)*\s*\)|(?!new\b)\w+)\s*)*}))?)*)\s*;'

wordpattern = re.compile(r"\w+")
patternsplitter = re.compile(r'(\w+)\s*(\[\s*\])?\s*(=\s*(new\s*\w+\s*(\(\s*\)|\[\s*\d+\s*\])|{[^}]+}|\"([^"]|\\.)*\"|(\w|\')*))?\s*(\,|\;)')
intpattern = re.compile(r'(int|long|short)\s*(\[\s*\]\s*\w+\s*(,\s*\w+|=(\s*{\s*\d+(\s*,\s*\d+\s*)*}|\s*(new\s+\1\s*\[\s*\d+\s*\])))?\s*(,\s*\w+\s*(\[\s*\])?\s*(=(\s*{\s*\d+(\s*,\s*\d+\s*)*}|\s*(new\s+\1\s*\[\s*\d+\s*\])))?)*|\s+\w+\s*(,\s*\w+|=\s*\d+|\[\s*\]\s*(=(\s*(new\s+\1\s*\[\s*\d+\s*\])|\s*{\s*\d+(\s*,\s*\d+\s*)*}))?)?(,\s*\w+|,\s*\w+\s*=\s*\d+|\s*\[\s*\]\s*(=(\s*(new\s+\1\s*\[\s*\d+\s*\])|(\s*{\s*\d+(\s*,\s*\d+\s*)*})))?)*)\s*;') #tipo int estandar, que puede hacer arreglos si se desea
doublepattern = re.compile(r'(double|float)\s*(\[\s*\]\s*\w+\s*(,\s*\w+|=(\s*(new\s+\1\s*\[\s*[1-9]\d*\s*\])|\s*{\s*[+-]?([0-9]*[.]?)[0-9]+(\s*,\s*[+-]?([0-9]*[.]?)[0-9]+\s*)*}))?\s*(,\s*\w+\s*(\[\s*\])?\s*(=(\s*(new\s+\1\s*\[\s*[1-9]\d*\s*\])|\s*{\s*[+-]?([0-9]*[.]?)[0-9]+(\s*,\s*[+-]?([0-9]*[.]?)[0-9]+\s*)*}))?)*|\w+\s*(,\s*\w+|=(\s*(new\s+\1\s*\[\s*[1-9]\d*\s*\])|\s*[+-]?([0-9]*[.]?)[0-9]+|\[\s*\]\s*(=\s*{\s*[+-]?([0-9]*[.]?)[0-9]+(\s*,\s*[+-]?([0-9]*[.]?)[0-9]+\s*)*})?))?(,\s*\w+|,\s*\w+\s*=\s*[+-]?([0-9]*[.]?)[0-9]+|\s*\[\s*\]\s*(=(\s*(new\s+\1\s*\[\s*[1-9]\d*\s*\])|\s*{\s*[+-]?([0-9]*[.]?)[0-9]+(\s*,\s*[+-]?([0-9]*[.]?)[0-9]+\s*)*}))?)*)\s*;')
stringpattern = re.compile(r'(String)\s*(\[\s*\]\s*\w+\s*(,\s*\w+|=(\s*(new\s+\1\s*\[\s*[1-9]\d*\s*\])|\s*{\s*\"[^"]*\"\s*(\s*,\s*\"[^"]*\"\s*)*}))?\s*(,\s*\w+\s*(\[\s*\])?\s*(=(\s*(new\s+\1\s*\[\s*[1-9]\d*\s*\])|\s*{\s*\"[^"]*\"\s*(\s*,\s*\"[^"]*\"\s*)*}))?)*|\w+\s*(,\s*\w+|=(\s*(new\s+\1\s*\[\s*[1-9]\d*\s*\])|\s*\"[^"]*\"\s*|\[\s*\]\s*(=\s*{\s*\"[^"]*\"\s*(\s*,\s*\"[^"]*\"\s*)*})?))?(,\s*\w+|,\s*\w+\s*=\s*\"[^"]*\"\s*|\s*\[\s*\]\s*(=(\s*(new\s+\1\s*\[\s*[1-9]\d*\s*\])|\s*{\s*\"[^"]*\"\s*(\s*,\s*\"[^"]*\"\s*)*}))?)*)\s*;')
charpattern = re.compile(r"(char)\s*(\[\s*\]\s*\w+\s*(,\s*\w+|=(\s*(new\s+\1\s*\[\s*[1-9]\d*\s*\])|\s*{\s*\'[^']\'\s*(\s*,\s*\'[^']\'\s*)*}))?\s*(,\s*\w+\s*(\[\s*\])?\s*(=(\s*(new\s+\1\s*\[\s*[1-9]\d*\s*\])|\s*{\s*\'[^']\'\s*(\s*,\s*\'[^']\'\s*)*}))?)*|\w+\s*(,\s*\w+|=\s*\'[^']\'\s*|\[\s*\]\s*(=(\s*(new\s+\1\s*\[\s*[1-9]\d*\s*\])|\s*{\s*\'[^']\'\s*(\s*,\s*\'[^']\'\s*)*}))?)?(,\s*\w+|,\s*\w+\s*=\s*\'[^']\'\s*|\s*\[\s*\]\s*(=(\s*(new\s+\1\s*\[\s*[1-9]\d*\s*\])|\s*{\s*\'[^']\'\s*(\s*,\s*\'[^']\'\s*)*}))?)*)\s*;")
booleanpattern = re.compile(r'(boolean)\s*(\[\s*\]\s*\w+\s*(,\s*\w+|=(\s*(new\s+\1\s*\[\s*[1-9]\d*\s*\])|\s*{\s*(true|false)\s*(\s*,\s*(true|false)\s*)*}))?\s*(,\s*\w+\s*(\[\s*\])?\s*(=(\s*(new\s+\1\s*\[\s*[1-9]\d*\s*\])|\s*{\s*(true|false)\s*(\s*,\s*(true|false)\s*)*}))?)*|\w+\s*(,\s*\w+|=\s*(true|false)\s*|\[\s*\]\s*(=(\s*(new\s+\1\s*\[\s*[1-9]\d*\s*\])|\s*{\s*(true|false)\s*(\s*,\s*(true|false)\s*)*}))?)?(,\s*\w+|,\s*\w+\s*=\s*(true|false)\s*|\s*\[\s*\]\s*(=(\s*(new\s+\1\s*\[\s*[1-9]\d*\s*\])|\s*{\s*(true|false)\s*(\s*,\s*(true|false)\s*)*}))?)*)\s*;')
bytepattern = re.compile(r'(byte)\s+(\[\s*\]\s*\w+\s*(,\s*\w+|=(\s*(new\s+\1\s*\[\s*[1-9]\d*\s*\])|\s*{\s*(0b[01]{1,8}|0x[0-9a-fA-F]{1,2}|\d{1,3})\s*(\s*,\s*(0b[01]{1,8}|0x[0-9a-fA-F]{1,2}|\d{1,3})\s*)*}))?\s*(,\s*\w+\s*(\[\s*\])?\s*(=(\s*(new\s+\1\s*\[\s*[1-9]\d*\s*\])|\s*{\s*(0b[01]{1,8}|0x[0-9a-fA-F]{1,2}|\d{1,3})\s*(\s*,\s*(0b[01]{1,8}|0x[0-9a-fA-F]{1,2}|\d{1,3})\s*)*}))?)*|\w+\s*(,\s*\w+|=\s*(0b[01]{1,8}|0x[0-9a-fA-F]{1,2}|\d{1,3})\s*|\[\s*\]\s*(=(\s*(new\s+\1\s*\[\s*[1-9]\d*\s*\])|\s*{\s*(0b[01]{1,8}|0x[0-9a-fA-F]{1,2}|\d{1,3})\s*(\s*,\s*(0b[01]{1,8}|0x[0-9a-fA-F]{1,2}|\d{1,3})\s*)*}))?)?(,\s*\w+|,\s*\w+\s*=\s*(0b[01]{1,8}|0x[0-9a-fA-F]{1,2}|\d{1,3})\s*|\s*\[\s*\]\s*(=(\s*(new\s+\1\s*\[\s*[1-9]\d*\s*\])|\s*{\s*(0b[01]{1,8}|0x[0-9a-fA-F]{1,2}|\d{1,3})\s*(\s*,\s*(0b[01]{1,8}|0x[0-9a-fA-F]{1,2}|\d{1,3})\s*)*}))?)*)\s*;')
objectpattern = re.compile(r'(Object)\s*(\[\s*\]\s*\w+\s*(,\s*\w+|=(\s*(new\s+\1\s*\[\s*[1-9]\d*\s*\])|\s*{\s*(new\s+\1\s*\(\s*([^,]?\w+[^,]?\s*(,\s*[^,]?\w+[^,]?)*)*\s*\)|(?!new\b)\w+)\s*(\s*,\s*(new\s+\1\s*\(\s*([^,]?\w+[^,]?\s*(,\s*[^,]?\w+[^,]?)*)*\s*\)|(?!new\b)\w+)\s*)*}))?\s*(,\s*\w+\s*(\[\s*\])?\s*(=(\s*(new\s+\1\s*\[\s*[1-9]\d*\s*\])|\s*{\s*(new\s+\1\s*\(\s*([^,]?\w+[^,]?\s*(,\s*[^,]?\w+[^,]?)*)*\s*\)|(?!new\b)\w+)\s*(\s*,\s*(new\s+\1\s*\(\s*([^,]?\w+[^,]?\s*(,\s*[^,]?\w+[^,]?)*)*\s*\)|(?!new\b)\w+)\s*)*}))?)*|\w+\s*(,\s*\w+|=\s*(new\s+\1\s*\(\s*([^,]?\w+[^,]?\s*(,\s*[^,]?\w+[^,]?)*)*\s*\)|(?!new\b)\w+)\s*|\[\s*\]\s*(=(\s*(new\s+\1\s*\[\s*[1-9]\d*\s*\])|\s*{\s*(new\s+\1\s*\(\s*([^,]?\w+[^,]?\s*(,\s*[^,]?\w+[^,]?)*)*\s*\)|(?!new\b)\w+)\s*(\s*,\s*(new\s+\1\s*\(\s*([^,]?\w+[^,]?\s*(,\s*[^,]?\w+[^,]?)*)*\s*\)|(?!new\b)\w+)\s*)*}))?)?(,\s*\w+|,\s*\w+\s*=\s*(new\s+\1\s*\(\s*([^,]?\w+[^,]?\s*(,\s*[^,]?\w+[^,]?)*)*\s*\)|(?!new\b)\w+)\s*|\s*\[\s*\]\s*(=(\s*(new\s+\1\s*\[\s*[1-9]\d*\s*\])|\s*{\s*(new\s+\1\s*\(\s*([^,]?\w+[^,]?\s*(,\s*[^,]?\w+[^,]?)*)*\s*\)|(?!new\b)\w+)\s*(\s*,\s*(new\s+\1\s*\(\s*([^,]?\w+[^,]?\s*(,\s*[^,]?\w+[^,]?)*)*\s*\)|(?!new\b)\w+)\s*)*}))?)*)\s*;')
bigpattern = re.compile('(int|long|short|double|float|String|char|boolean|byte|Object)('+Pstring+'|'+Pchar+'|'+Pint+'|'+Pdouble+'|'+Pboolean+'|'+pbyte+'|'+pObject+')')

patterns = [stringpattern,charpattern,intpattern,doublepattern,booleanpattern,bytepattern,objectpattern]
for pattern in patterns:
  for match in pattern.finditer(text):
      # print(match)

      # #int/float/string
      # print(match.group(1))

      #Crea la llave si aún no está en el diccionario
      #[escalares Declaradas no Inicializadas, escalares Inicializadas, arreglos Dec y no Inicializadas, arreglos Inicializados]
      if (d.get(match.group(1)) is None):
        d[match.group(1)]=[0,0,0,0]
        variables[match.group(1)] = []
      
      #group(0) tiene la cadena completa
      #El split(',') entrega cada una de las declaraciones 
      #si la expresion es int a, b, c, d[]
      #regresa:
      #int a
      #b
      #c
      #d[]
      cadena = match.group(0)[len(match.group(1)):]
      flag = False
      for c in cadena:
        if(c == '['):
          flag=True
        elif( not c== ' '):
          break


      for wordmatch in patternsplitter.finditer(cadena):
        
        word = wordmatch.group(0)
        # print(word)
        variablematch = wordpattern.search(word)
        if variablematch: #push del nombre de la variable en la lista del tipo
          variables[match.group(1)].append(variablematch.group(0))
          # print("match : "+str(variablematch))

        #Si encuentras '[' Es un arreglo
        if("[" in word or flag):
          #Si ademas hay una asignación, está inicializado
          if("=" in word):
            d[match.group(1)][3]+=1
          else:
            #Si no, solo está declarado
            d[match.group(1)][2]+=1
        else:
          #Si no está, es un escalar
          if("=" in word):
            #Si aparece = es una asignación
            d[match.group(1)][1]+=1
          else:
            #Si no, está declarado pero no inicializado
            d[match.group(1)][0]+=1
        # print(d)
        text = text.replace(match.group(0),'',1)
        # print(text)

# print(d)
# print(variables)



# In[12]:



def tabula(dic):
    
    
    dd = {}
    num_keys = len(dic)
    dd['Tipo de Dato']= ['']*num_keys
    dd['Declaradas']=[0]*num_keys
    dd['Inicializadas']=[0]*num_keys
    dd['Array Declarados']=[0]*num_keys
    dd['Array Inicializados']=[0]*num_keys
    dd['Total/Tipo']=[0]*num_keys
    cont = 0
    
    for typeData in dic:
        #Este es el total por tipo
        total = sum(dic[typeData])
        dd['Tipo de Dato'][cont] = typeData
        dd['Declaradas'][cont]=dic[typeData][0]
        dd['Inicializadas'][cont]=dic[typeData][1]
        dd['Array Declarados'][cont]=dic[typeData][2]
        dd['Array Inicializados'][cont]=dic[typeData][3]
        dd['Total/Tipo'][cont] = total
        cont+=1 
        
    total_variables = sum(dd['Total/Tipo'])
    total_tipos = len(dd['Tipo de Dato'])
    
        
    return dd,[total_variables,total_tipos]
def render_mpl_table(data, col_width=3.0, row_height=0.625, font_size=14,
                     header_color='#40466e', row_colors=['#f1f1f2', 'w'], edge_color='w',
                     bbox=[0, 0, 1, 1], header_columns=0,
                     ax=None, **kwargs):
    if ax is None:
        size = (np.array(data.shape[::-1]) + np.array([0, 1])) * np.array([col_width, row_height])
        fig, ax = plt.subplots(figsize=size)
        ax.axis('off')

    mpl_table = ax.table(cellText=data.values, bbox=bbox, colLabels=data.columns, **kwargs)

    mpl_table.auto_set_font_size(False)
    mpl_table.set_fontsize(font_size)

    for k, cell in  six.iteritems(mpl_table._cells):
        cell.set_edgecolor(edge_color)
        if k[0] == 0 or k[1] < header_columns:
            cell.set_text_props(weight='bold', color='w')
            cell.set_facecolor(header_color)
        else:
            cell.set_facecolor(row_colors[k[0]%len(row_colors) ])
    ax.set_title('Reconocedor de Declaraciones',size=20)
    fig.savefig('tabla.png')
    
    return ax



# In[13]:

resultados = tabula(d)
df = pd.DataFrame(resultados[0])
ax = render_mpl_table(df, header_columns=0, col_width=3)


print("\nRESULTADOS: ")
print('')
print('Total de variables declaradas: ', resultados[1][0])
print('Total de tipos de datos usados: ', resultados[1][1])
print('')



print('Nombres de Variables por Tipo: ')
for typeData in variables:
    print (typeData.upper(),': ')
    i = 1
    for variable in variables[typeData]:
        print(i,': ',variable)
        i+=1
        
    print('------------------------------------------------------------------')
        
#print(variables)
print('')
print('A continuación se despliega una tabla con la información de cada tipo de dato')

ax.plot()





# In[ ]:




