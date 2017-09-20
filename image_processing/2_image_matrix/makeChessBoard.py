# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 10:52:12 2015

@author: erts
"""

############################################
## Import OpenCV
import numpy as np
import cv2
############################################

############################################
## Read the image
fullPattern = np.zeros((400,400),np.uint8)
fullPattern[200:400,0:200]=255
fullPattern[0:200,200:400]=255



############################################

############################################
## Do the processing
############################################

############################################
## Show the image
cv2.imshow('canvas', fullPattern)
############################################

############################################
## Close and exit
while(1):
       key= cv2.waitKey(1)
       if (key & 0xFF) == 27:
           break

cv2.destroyAllWindows()
############################################
