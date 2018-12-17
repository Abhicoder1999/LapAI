# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 15:10:35 2018

@author: abhijeet
"""

import cv2
import numpy as np
from pynput.mouse import Button, Controller
import wx

#Initial Setup
mouse=Controller()
app=wx.App(False)
(sx,sy)=wx.GetDisplaySize()
(camx,camy)=(320,240)

lowerBound=np.array([0,119,153])
upperBound=np.array([35,255,255])

cam= cv2.VideoCapture(0)
kernelOpen=np.ones((5,5))
kernelClose=np.ones((10,10))
pinchFlag=0

while True:

# Image Processing
    ret, img=cam.read()
    img=cv2.resize(img,(340,220))

    #convert BGR to HSV
    imgHSV= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    # create the Mask
    mask=cv2.inRange(imgHSV,lowerBound,upperBound)
    #morphology
    maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
    maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)

    maskFinal=maskClose
    cv2.imshow("mask",maskFinal)
    _,conts,_=cv2.findContours(maskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
#Functionality
    #Mouse Hovering Function
    if(len(conts)>0):
        c = max(conts, key = cv2.contourArea)
        (x,y),radius = cv2.minEnclosingCircle(c)
        center = (int(x),int(y))
        print(x,y)
        radius = int(radius)
        cv2.circle(img,center,radius,(0,255,0),2)
        cv2.imshow("cam",img)
        mouseLoc=(sx-(x*sx/camx), y*sy/camy)
        mouse.position=mouseLoc
        #while mouse.position!=mouseLoc:
          # continue


#Breaking Condition
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cam.release()
del app
cv2.destroyAllWindows()
cv2.waitKey(0)
cv2.waitKey(0)
cv2.waitKey(0)
cv2.waitKey(0)
cv2.waitKey(0)
cv2.waitKey(0)
cv2.waitKey(0)
cv2.waitKey(0)
