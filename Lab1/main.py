import cv2, sys
path = "./Lab1/test.png"
while(1):
    img = cv2.imread(path, flags = cv2.IMREAD_COLOR)
    cv2.namedWindow("IMG", flags=cv2.WINDOW_FULLSCREEN)
    cv2.imshow("IMG", img)
    key = cv2.waitKey(5000)
    if key == 27:
        sys.exit(1)
    cv2.destroyWindow("IMG")
    img = cv2.imread(path, flags = cv2.IMREAD_GRAYSCALE)
    cv2.namedWindow("IMG", flags=cv2.WINDOW_FULLSCREEN)
    cv2.imshow("IMG", img)
    key = cv2.waitKey(7000)
    if key == 27:
        sys.exit(1)
    cv2.destroyWindow("IMG")
    img = cv2.imread(path, flags = cv2.IMREAD_REDUCED_COLOR_2)
    cv2.namedWindow("IMG", flags=cv2.WINDOW_GUI_NORMAL)
    cv2.imshow("IMG", img)
    key = cv2.waitKey(9000)
    if key == 27:
        sys.exit(1)
    cv2.destroyWindow("IMG")
    img = cv2.imread(path, flags = cv2.IMREAD_REDUCED_GRAYSCALE_4)
    cv2.namedWindow("IMG", flags=cv2.WINDOW_GUI_NORMAL)
    cv2.imshow("IMG", img)
    key = cv2.waitKey(11000)
    if key == 27:
        sys.exit(1)
    cv2.destroyWindow("IMG")
    img = cv2.imread(path, flags = cv2.IMREAD_COLOR)
    [b, g, r] = cv2.split(img)
    img = cv2.merge((b,r,g))
    # img[:,:,1], img[:,:,2] = img[:,:,2], img[:,:,1]
    cv2.namedWindow("IMG", flags=cv2.WINDOW_FULLSCREEN)
    cv2.imshow("IMG", img)
    key = cv2.waitKey(4000)
    cv2.destroyAllWindows()
    if key == 27: 
        sys.exit(1)