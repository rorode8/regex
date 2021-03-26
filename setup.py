# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 15:23:12 2021

@author: rorod
"""
import pip

packages = ['re',  'numpy', 'pandas', 'matplotlib', 'six']

def import_or_install(package):
    try:
        __import__(package)
        print(package+" is present")
    except ImportError:
        print("library "+package+" is not present, trying to install it")
        pip.main(['install', package])       
        
for p in packages:
    import_or_install(p)