import cv2, time

cam = cv2.VideoCapture(0)

while True:
    ret,img = cam.read()
    cv2.imshow('Camera', img)
    key = cv2.waitKey(10)
    if key == ord(' '):
        time.sleep(1000)