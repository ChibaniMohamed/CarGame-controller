import cv2
import numpy as np
import time
from pynput.keyboard import Key, Controller
#import urllib
#import requests
keyboard = Controller()
cap = cv2.VideoCapture(0+cv2.CAP_DSHOW)
while True:
 _,test_img = cap.read()
 frame_gau_blur = cv2.blur(test_img, (13, 13))
 hsvimg = cv2.cvtColor(frame_gau_blur,cv2.COLOR_BGR2HSV)
 low_green = np.array([30,100,100])
 high_green = np.array([80, 255, 255])
 green_in_img = cv2.inRange(hsvimg,low_green,high_green)
 mask1 = cv2.bitwise_and(frame_gau_blur,frame_gau_blur,mask=green_in_img)
 gray = cv2.cvtColor(mask1,cv2.COLOR_BGR2GRAY)
 kernel = np.ones((5,5),np.uint8)
 mask = cv2.morphologyEx(gray,cv2.MORPH_ELLIPSE,kernel)
 ret, thresh = cv2.threshold(mask, 70, 255, 0)
 contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
 font = cv2.FONT_HERSHEY_COMPLEX
 fontsize = 2
 color = (255,255,255)
 thickness = 3
 right = cv2.rectangle(test_img,(350,200),(600,400),(255,255,255),4)
 cv2.putText(right,"RIGHT",(380,320),font,fontsize,color,thickness)
 left = cv2.rectangle(test_img,(0,200),(250,400),(255,255,255),4)
 cv2.putText(left,"LEFT",(30,320),font,fontsize,color,thickness)
 for cts in contours:
  (x,y,w,h) = cv2.boundingRect(cts)
  x2 = x + w/2
  y2 = y + h/2
  cv2.rectangle(test_img,(x,y),(x+w,y+h),(0,0,255),2)
  cv2.circle(test_img,(int(x2),int(y2)),1,(0,0,255),5)
  if x2 and y2 :
   keyboard.press(Key.up)
   if x2 > 350 and y2 > 200 :
      keyboard.press(Key.right)

   else :
      keyboard.release(Key.right)

   if x2 < 250 and y2 < 400 :
      keyboard.press(Key.left)

   else :
      keyboard.release(Key.left)
 else:
      keyboard.release(Key.up)
      #keyboard.press(Key.down)
 cv2.imshow("test",test_img)
 if cv2.waitKey(1) & 0xFF == ord('q'):
     break
     cv2.destroyAllWindows()
