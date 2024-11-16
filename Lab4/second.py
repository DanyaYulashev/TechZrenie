import cv2, numpy as np
path = './Lab4/4-2.jpg'

img = cv2.imread(path, flags = cv2.IMREAD_COLOR)

ker = np.full((9, 9), 0.1)

img_morph = cv2.morphologyEx(img, op = cv2.MORPH_BLACKHAT, kernel = ker, anchor = (-1, -1), iterations = 2, borderType = cv2.BORDER_DEFAULT)
cv2.namedWindow("IMG", flags = cv2.WINDOW_AUTOSIZE)
cv2.imshow("IMG", img_morph)
key = cv2.waitKey(0)