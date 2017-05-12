#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import xml.etree.ElementTree as ET

tree = ET.parse("test.xml")
root = tree.getroot()
print(root.tag)

for child in root:
    print("\t", child.tag, child.attrib, child.text)
    for i in child:
        print("\t\t", i.tag, i.attrib, i.text)

