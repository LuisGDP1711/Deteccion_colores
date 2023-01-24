import cv2
import numpy as np

def Area_Saludable(ret, image, verde_bajo, verde_alto, mascara):
    global area_saludable2
    if ret:
        image = cv2.flip(image, 1)
        imagenHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        mascara = cv2.inRange(imagenHSV, verde_bajo, verde_alto)

        #---------------CONTORNO-------------
        contornos, _ = cv2.findContours(mascara,  cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # cv2.drawContours(image, contornos, -1, (255,0,0), 4)

        for c in contornos:
            area_saludable2 = cv2.contourArea(c)   
    return area_saludable2
