import cv2
path = './Lab2/2-1.jpg'
img = cv2.imread(path, flags=cv2.IMREAD_GRAYSCALE)
new_img = cv2.adaptiveThreshold(img, 255, adaptiveMethod=cv2.ADAPTIVE_THRESH_MEAN_C, thresholdType=cv2.THRESH_BINARY, blockSize=21, C=11)
cv2.namedWindow("IMG", flags = cv2.WINDOW_AUTOSIZE)
cv2.imshow("IMG", new_img)
key = cv2.waitKey(0)
cv2.destroyAllWindows()