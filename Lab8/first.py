import cv2

path = './Lab8/task.png'

img = cv2.imread(path, flags = cv2.IMREAD_COLOR)

img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, imgBin = cv2.threshold(img2, 250, 255, type = cv2.THRESH_BINARY)

ans = cv2.findContours(imgBin, mode = cv2.RETR_CCOMP, method = cv2.CHAIN_APPROX_SIMPLE)
contours, _ = ans

pattern = contours[1]
cv2.drawContours(img, contours, contourIdx = 1, color = [255, 255, 0], thickness = 3, lineType = cv2.LINE_8)

patternMoments = cv2.moments(contours[1], binaryImage = False)
patternHuMoments = cv2.HuMoments(patternMoments)
patternm00 = patternMoments['m00']
diff = 1e-3
difference = []
for i in range(2, len(contours)):
    Moments = cv2.moments(contours[i], binaryImage = False)
    HuMoments = cv2.HuMoments(Moments)
    momentm00 = Moments['m00']
    differencem00 = abs(patternm00 - momentm00)
    difference[:] = abs(patternHuMoments[:] - HuMoments[:])
    if (difference[0] <= diff) & (difference[1] <= diff) &\
        (difference[2] <= diff) & (difference[3] <= diff):
        if (0.95*patternm00 <= momentm00 <= 1.05*patternm00):
            cv2.drawContours(img, contours, contourIdx = i, color = [255, 0, 139], thickness = 3, lineType = cv2.LINE_8)

cv2.namedWindow("IMG", flags = cv2.WINDOW_GUI_EXPANDED)
cv2.imshow("IMG", img)
key = cv2.waitKey()
cv2.destroyAllWindows()