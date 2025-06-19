import cv2
import numpy as np
#bhaskar 1
#ganshyam 2
# raghav 3
# yash 4
# omkar 5
# chintan 6
# #

image1 = cv2.imread(r'D:\project X\venv\2apptitude test\Bhaskar2.jpg')

image1 = cv2.resize(image1, (300, 400))  

image2 = cv2.imread(r'D:\project X\venv\2apptitude test\Ganshyam2.jpg')
image2 = cv2.resize(image2, (300, 400)) 

image3 = cv2.imread(r'D:\project X\venv\2apptitude test\Raghav2.jpg')
image3 = cv2.resize(image3, (300, 400)) 

image4 = cv2.imread(r'D:\project X\venv\2apptitude test\Yash2.png')
image4 = cv2.resize(image4, (300, 400)) 

image5 = cv2.imread(r'D:\project X\venv\2apptitude test\Om2.png')
image5 = cv2.resize(image5, (300, 400)) 

image6 = cv2.imread(r'D:\project X\venv\2apptitude test\Chintan2.png')
image6 = cv2.resize(image6, (300, 400)) 

imgs = [image1, image2, image3, image4, image5, image6]

def showoriginals():
    
    cv2.imshow('image1 ',image1)
    cv2.imshow('image2 ',image2)
    cv2.imshow('image3 ',image3)
    cv2.imshow('image4 ',image4)
    cv2.imshow('image5 ',image5)
    cv2.imshow('image6 ',image6)
    return 

showoriginals()




def brighten(img , value):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    img[:, :, 2] = img[:, :, 2] * value
    img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)

    return  img

def grayof(img):
    gimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    return gimg

def threshof(img):
    img = grayof(img)
    _, threshimg = cv2.threshold(img, 10, 255, cv2.THRESH_BINARY)
    return threshimg

def addimage(img1,img2,img3):
    add=cv2.add(img1,img2,img3)
    return add
def invert(img):
    img = 255-img
    return img
image1brighter= brighten(image1,100)
image2brighter= brighten(image2,100)
image3brighter= brighten(image3,100)
cv2.imshow('image 1 but brighter', image1brighter)
cv2.imshow('image 2 but brighter', image2brighter)
cv2.imshow('image 3 but brighter', image3brighter)
image4brighter= brighten(image4,100)
image5brighter= brighten(image5,100)
image6brighter= brighten(image6,100)
cv2.imshow('image 4 but brighter', image4brighter)
cv2.imshow('image 5 but brighter', image5brighter)
cv2.imshow('image 6 but brighter', image6brighter)
add123=addimage(image1brighter,image2brighter,image3brighter)
cv2.imshow('addition of bright of 1 2 3 ',add123)
add456=addimage(image4brighter,image5brighter,image6brighter)
cv2.imshow('addition of bright of 4 5 6  ',add456)
cv2.imshow("invert 1 brighter", invert(image1brighter))
cv2.imshow("invert 1", invert(image1))
addedall= cv2.add(add123,add456)
cv2.imshow("cumulation of all images",addedall)
cv2.waitKey(0)
cv2.destroyAllWindows()


