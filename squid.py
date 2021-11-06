'''
Author: Yogi/Vegeta2007k
'''

# The code below will use opencv to detect movement
'''
This will not really kill anyone(sadly), but instead, play a 'beep' sound when detects motion...
The Beep sound will be within the repository with the name 'Alert.wav'...
You can download it if you want...or even use some other sound
'''

import cv2
import winsound
cum = cv2.VideoCapture(0)
while cum.isOpened():
    ret, frame1 = cum.read()
    ret, frame2 = cum.read()
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
  
  
    for c in contours:
        if cv2.contourArea(c) < 3000:
            continue
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        winsound.PlaySound('alert.wav', winsound.SND_ASYNC)
    if cv2.waitKey(10) == ord('q'):
        break
    cv2.imshow('Your Mom LOL', frame1)
