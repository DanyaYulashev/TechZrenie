import cv2, numpy as np
from math import pi

def draw_line(x0, y0, x1, y1, img, color = (0, 139, 0), thickness = 3, lineType = cv2.LINE_8):
    cv2.line(img, (x0,y0), (x1,y1), color, thickness, lineType)

path = './Lab5/video1.mp4'
vid = cv2.VideoCapture(path)
framenumber = 0
while(True):
    ret, frame =  vid.read()
    if ret:
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, edges = cv2.threshold(img, 110, 255, type = cv2.THRESH_BINARY)
        lines = cv2.HoughLinesP(edges, rho = 5, theta = pi/180, threshold = 700, minLineLength = None, maxLineGap = None)
        img2 = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        for i in range(0, len(lines)):
            x0,y0,x1,y1 = lines[i][0][:]
            draw_line(x0, y0, x1, y1, img2)
        cv2.namedWindow("IMG", flags = cv2.WINDOW_NORMAL)
        cv2.imshow("IMG", img2)
        key = cv2.waitKey(1)
        framenumber += 1
    else:
        break
vid.release()
cv2.destroyAllWindows()