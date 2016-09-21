#!/usr/bin/python
#-*- coding:utf-8 -*-
#'''
#This example illustrates how to use cv2.HoughCircles() function.

#Usage:
#    houghcircles.py [<image_name>]
#    image argument defaults to ../data/board.jpg
#'''

# Python 2/3 compatibility
from __future__ import print_function

import cv2
import numpy as np
import sys

if __name__ == '__main__':
    print(__doc__)

#Paramètres de la camera, temporaire pour le test sur PC########################

res = (1280,720)
cap = cv2.VideoCapture(0)
cap.set(3,res[0])
cap.set(4,res[1])
center = (res[0]/2,res[1]/2)
################################################################################
def CartesianLine(frame,pt1,pt2,thickness):
    cv2.line(frame, (int(center[0]+pt1[0]),
                    int(center[1]-pt1[1])),
                    (int(center[0]+pt2[0]),
                    int(center[1]-pt2[1])), 
                    (0,255,0), 
                    thickness)

def DrawCenterDot(frame,scaling):
    CartesianLine(frame,(0,0),(0,0),scaling)
    CartesianLine(frame,(0,0),(0,0),scaling)


while True:
    
    ret,src = cap.read()
    src= cv2.flip(src,1)
    img = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    img = cv2.medianBlur(img, 5)
    cimg = src.copy() # numpy function

    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 10, np.array([]), 100, 30, 1, 30)
    if circles != None :
        a, b, c = circles.shape
        
        for i in range(b):
            cv2.circle(cimg, (circles[0][i][0], circles[0][i][1]), circles[0][i][2], (0, 0, 255), 3, cv2.LINE_AA)
            cv2.circle(cimg, (circles[0][i][0], circles[0][i][1]), 2, (0, 255, 0), 3, cv2.LINE_AA)  # draw center of circle
        # Affiche centre cercle
        print ("Centre des cercles:")
        print (circles[0][i][0],circles[0][i][1])
        # Affiche ecart au centre de l'image
        #print ("Ecart au centre")
        dim = src.shape
        delta_x = dim[1]/2-circles[0][i][0]
        delta_y = dim[0]/2-circles[0][i][1]
        CartesianLine(cimg,(0,0),(-delta_x,delta_y),2);
        print (delta_x, delta_y)
        if (delta_x > 15):
            if (delta_x < 0):
                print ("Correction x : -")
            else:
                print ("Correction x : +")
        if (delta_y > 15):
            if (delta_y < 0):
                print ("Correction y : -")
            else:
                print ("Correction y : +")
        else:
            print ("Objet centre")
        DrawCenterDot(cimg,2)
        cv2.imshow("detected circles", cimg)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
