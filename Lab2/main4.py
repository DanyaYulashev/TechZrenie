import cv2
cap = cv2.VideoCapture(0)
while(1):
    ret, frame = cap.read()
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # new_img = cv2.adaptiveThreshold(img, 255, adaptiveMethod=cv2.ADAPTIVE_THRESH_MEAN_C, thresholdType=cv2.THRESH_BINARY, blockSize=11, C=7)
    threshold_new, new_img = cv2.threshold(img, 150, 255, type = cv2.THRESH_OTSU)
    cv2.imshow('frame',new_img)
    if cv2.waitKey(1) == 27:
        break