import cv2
path = './Lab5/5-4.png'
path2 = './Lab5/5-5.jpg'

img = cv2.imread(path, flags = cv2.IMREAD_REDUCED_GRAYSCALE_2)
img2 = cv2.imread(path2, flags = cv2.IMREAD_GRAYSCALE)

downthresh1 = 150
upthresh1 = 200

downthresh2 = 150
upthresh2 = 200

edges1 = cv2.Canny(img, downthresh1, upthresh1, apertureSize=3, L2gradient=False)
edges2 = cv2.Canny(img2, downthresh2, upthresh2, apertureSize=3, L2gradient=False)

cv2.namedWindow("IMG", flags = cv2.WINDOW_NORMAL)
cv2.imshow("IMG", edges1)
key = cv2.waitKey()
cv2.namedWindow("IMG", flags = cv2.WINDOW_NORMAL)
cv2.imshow("IMG", edges2)
key = cv2.waitKey()
cv2.destroyAllWindows()