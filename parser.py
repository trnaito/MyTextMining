# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 16:38:09 2016

@author: U6040067
"""
import os
import xml.etree.ElementTree as ET

# print(os.getcwd())

os.chdir(r"C:\Users\u6040067\Documents\GitHub\MyTextMining")
tree = ET.parse('test_to_read.xml')
root = tree.getroot()

# Print tag name
root.tag

# Print tag attribute
root.attrib

# Print Child tag & attribute
for child in root:
    print(child.tag, child.attrib)

# Itereate to print a specific tagged values
for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)
    
