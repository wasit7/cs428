# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 11:24:12 2014

@author: Wasit
"""

import numpy as np
import cv2

# Load an color image in grayscale
img =cv2.imread('../img/building.jpg',0)
cv2.imshow('sample image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('build_bg.jpg',img)