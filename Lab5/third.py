import cv2
path = './Lab5/video1.mp4'
vid = cv2.VideoCapture(path)
framenumber = 0
while(True):
    ret, frame =  vid.read()
    if ret:
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges1 = cv2.Canny(img, 100, 200, apertureSize=3, L2gradient=False)
        cv2.namedWindow("IMG", flags = cv2.WINDOW_NORMAL)
        cv2.imshow("IMG", edges1)
        key = cv2.waitKey(10)
        framenumber += 1
    else:
        break
vid.release()
cv2.destroyAllWindows()