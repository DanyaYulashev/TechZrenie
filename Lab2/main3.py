import cv2
path = './Lab2/2-3.png'
path2 = './Lab2/2-4.png'
img = cv2.imread(path, flags=cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(path2, flags = cv2.IMREAD_GRAYSCALE)
# new_img = cv2.adaptiveThreshold(img, 255, adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C, thresholdType=cv2.THRESH_BINARY, blockSize=21, C=5)
new_img2 = cv2.adaptiveThreshold(img2, 255, adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C, thresholdType=cv2.THRESH_BINARY, blockSize=21, C=31)
threshold_new, new_img = cv2.threshold(img2, 0, 255, type = cv2.THRESH_OTSU)
print(threshold_new)
 
cv2.namedWindow("IMG", flags = cv2.WINDOW_FULLSCREEN)
cv2.imshow("IMG", new_img)
key = cv2.waitKey(0)
cv2.namedWindow("IMG", flags = cv2.WINDOW_FULLSCREEN)
cv2.imshow("IMG", new_img2)
key = cv2.waitKey(0)
cv2.destroyAllWindows()