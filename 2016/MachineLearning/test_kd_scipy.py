# -*- coding: utf-8 -*-
"""
Created on Tue Dec 02 00:03:46 2014

@author: Wasit
"""
from scipy import spatial
data = [(1,2,3),(4,0,1),(5,3,1),(10,5,4),(9,8,9),(4,2,4)]
tree = spatial.KDTree(data)
d,ids=tree.query(data[0],k=6)
