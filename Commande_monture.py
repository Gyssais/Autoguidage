#!/usr/bin/python

'''
This example illustrates how to use cv2.HoughCircles() function.

Usage:
    houghcircles.py [<image_name>]
    image argument defaults to ../data/board.jpg
'''

# Python 2/3 compatibility
from __future__ import print_function

import cv2
import numpy as np
import sys

if __name__ == '__main__':
    print(__doc__)

    try:
        fn = sys.argv[1]
    except IndexError:
        fn = "venus-transit-soleil.jpg"

    src = cv2.imread(fn, 1)
    img = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    img = cv2.medianBlur(img, 5)
    cimg = src.copy() # numpy function

    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 10, np.array([]), 100, 30, 1, 30)
    a, b, c = circles.shape
    for i in range(b):
        cv2.circle(cimg, (circles[0][i][0], circles[0][i][1]), circles[0][i][2], (0, 0, 255), 3, cv2.LINE_AA)
        cv2.circle(cimg, (circles[0][i][0], circles[0][i][1]), 2, (0, 255, 0), 3, cv2.LINE_AA)  # draw center of circle
	# Affiche centre cercle
	print ("Centre cercles")
	print (circles[0][i][0])
	print (circles[0][i][1])
	# Affiche ecart au centre de l'image
	print ("Ecart au centre")
	dim = src.shape
	delta_x = dim[0]/2-circles[0][i][0]
	delta_y = dim[1]/2-circles[0][i][1]
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

    cv2.imshow("source", src)
    cv2.imshow("detected circles", cimg)
    cv2.waitKey(0)
