import cv2, numpy as np
path = './Lab4/4-1.jpg'

def closing_or_opening(operation,img, kernel, n_iterations):
    if operation == 1:
        img_new=cv2.dilate(img, kernel = kernel, anchor = (-1, -1), iterations = n_iterations, borderType = cv2.BORDER_DEFAULT)
        img_new=cv2.erode(img_new, kernel = kernel, anchor = (-1, -1), iterations = n_iterations, borderType = cv2.BORDER_DEFAULT)
        return(img_new)
    else:
        img_new=cv2.erode(img, kernel = kernel, anchor = (-1, -1), iterations = n_iterations, borderType = cv2.BORDER_DEFAULT)
        img_new=cv2.dilate(img_new, kernel = kernel, anchor = (-1, -1), iterations = n_iterations, borderType = cv2.BORDER_DEFAULT)
        return(img_new)

img = cv2.imread(path, flags = cv2.IMREAD_COLOR)

ker = np.full((3, 3),0.1)

my_img1 = closing_or_opening(1,img, ker, 2)
my_img2 = closing_or_opening(2,img, ker, 2)

img_morph1 = cv2.morphologyEx(img, op = cv2.MORPH_OPEN, kernel = ker, anchor = (-1, -1), iterations = 2, borderType = cv2.BORDER_DEFAULT)
img_morph2 = cv2.morphologyEx(img, op = cv2.MORPH_CLOSE, kernel = ker, anchor = (-1, -1), iterations = 2, borderType = cv2.BORDER_DEFAULT)

diff_img1 = my_img1-img_morph2
diff_img2 = my_img2-img_morph1

cv2.namedWindow("IMG", flags = cv2.WINDOW_AUTOSIZE)
cv2.imshow("IMG", img_morph1)

key = cv2.waitKey(0)
cv2.imshow("IMG", img_morph2)

key = cv2.waitKey(0)
