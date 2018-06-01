# -*- coding: utf-8 -*-
"""
Created on Wed Dec 03 18:50:34 2014

@author: Wasit
"""

#SIFT
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import os
import cv2

# read image to array
rootdir="../img"
all_files=[]
for root, dirs, files in os.walk(rootdir):
    for f in files:
            if f.endswith('jpg'):
                all_files.append(os.path.join(root,f))
#    for subdir in dirs:
#        for iroot,idirs,ifiles in os.walk(os.path.join(root,subdir)):
#            for f in ifiles:
#                if f.endswith('jpg'):
#                    all_files.append(os.path.join(iroot,f))
for im_file in all_files:
    print im_file
    im = np.array(Image.open(im_file).convert('L'))
    #SIFT
    sift = cv2.SIFT()
    kp, des = sift.detectAndCompute(im,None)
    img=cv2.drawKeypoints(im,kp,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    # Display the resulting frame
    cv2.imshow('SIFT',img)
    if cv2.waitKey(1000) & 0xFF == ord('q'):
        break

