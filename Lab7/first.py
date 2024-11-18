import cv2, math

def draw_line(rho, theta, img, color=(255, 255, 255), thickness = 15, lineType = cv2.LINE_AA):
    cos_t = math.cos(theta)
    sin_t = math.sin(theta)
    x0 = cos_t * rho
    y0 = sin_t * rho
    pt1 = int(x0 - 1000*sin_t), int(y0 - 1000*cos_t)
    pt2 = int(x0 + 1000*sin_t), int(y0 + 1000*cos_t)
    cv2.line(img, pt1, pt2, color, thickness, lineType)

path = './Lab7/7_1.jpg'

img = cv2.imread(path, flags = cv2.IMREAD_GRAYSCALE)

_, img2 = cv2.threshold(img, 75, 255, type = cv2.THRESH_BINARY_INV)

lines = cv2.HoughLines(img2, rho = 1, theta = math.pi/180, threshold = 700, min_theta = None, max_theta = None)

for i in range(0, len(lines)):
    rho = lines[i][0][0]
    theta = lines[i][0][1]
    draw_line(rho, theta, img = img)

cv2.namedWindow("IMG", flags = cv2.WINDOW_AUTOSIZE)
cv2.imshow("IMG", img2)
key =cv2.waitKey()
cv2.namedWindow("IMG", flags = cv2.WINDOW_AUTOSIZE)
cv2.imshow("IMG", img)
key = cv2.waitKey()