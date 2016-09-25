#!/usr/bin/python

# Python 2/3 compatibility
from __future__ import print_function

import cv2
import numpy as np
import sys

def detect_reperes (fn):
    # Ouverture de l'image
    src = cv2.imread(fn, 1)
    # Conversion de l'image en niveau de gris
    img = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    dim = img.shape # Dimensions de l'image
    img2 = img.copy()

    # Parcours de l'image pour ne garder que les pixels blancs = etoiles (au dela d'un certain seuil)
    # Ajout d'un cercle blanc de 4 pixels de rayon autour de chaque pixel blanc. Operation necessaire pour une detection efficace des bords.
    for i in range(dim[0]):
        for n in range(dim[1]):
            if (img.item(i,n)) > 150 :
                img2.itemset((i,n), 255)
                img2 = cv2.circle(img2,(i,n), 4, 255, -1)
                print (i,n)
            else:
                img2.itemset((i,n), 0)  
    
    imgSeuil = img2.copy()

    # detections des contours
    image, contours, hierarchy = cv2.findContours(img2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    # dessin des contours (ca marche pas, pourquoi ?)
    imgCnt = cv2.drawContours(img2, contours, -1, (0,255,0), 3)

    imgN = np.zeros((dim[0],dim[1],3), np.uint8) # Image noire

    listeCentroid = []
    # Calcul des moments des contours, ce qui permet de calculer les centres des contours
    # On obtient ainsi la position d'un certain nombre d'etoiles dans l'image
    for cnt in contours:
        M = cv2.moments(cnt)
        #print (M)
        if M['m00'] != 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            listeCentroid = listeCentroid + [(cx,cy)]
            #print (cx, cy)
            imgN = cv2.circle(imgN, (cx,cy), 5, (255,0,0), -1)


    cv2.imshow('NB',src)
    cv2.imshow('Seuil', imgSeuil)
    cv2.imshow('imageContours',imgCnt)
    cv2.imshow('etoiles',imgN)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return listeCentroid


def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)
	
# Detection des etoiles dans deux images identiques mais decales de 5 pixels en X et en Y
l1 = detect_reperes("etoiles1_small.jpg")
l2 = detect_reperes("etoiles2_small.jpg")

l_ecartX = []
l_ecartY = []

# recherche des reperes de la premiere image dans la deuxieme
# les reperes sont consideres correspondant lorsqu'il y a moins de 10 pixels d'ecart entre les deux
for i in l1:
    for n in l2:
        ecartX = (n[0]-i[0])
        ecartY = (n[1]-i[1])
        if (ecartX < 10 and ecartX > -10 and ecartY < 10 and ecartY > -10):
            # Meme repre, qui a plus ou moins bouge
            l_ecartX = l_ecartX + [ecartX]
            l_ecartY = l_ecartY + [ecartY]
            break

# Calcul de l'ecart moyen entre les reperes
print (mean(l_ecartX))
print (mean(l_ecartY))


