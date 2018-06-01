# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 11:39:51 2014

@author: Wasit
"""
import numpy as np
import cv2

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
cv2.line(img,(0,0),(511,511),(255,0,0),5)
cv2.imshow('line',img)
