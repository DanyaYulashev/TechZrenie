import cv2, numpy as np
res = np.full((700, 1000, 3), (255, 255, 255), dtype = np.uint8)
cv2.namedWindow("IMG", flags=cv2.WINDOW_FULLSCREEN)
cv2.line(res, (0, 700), (1000, 0), (255, 191, 0), 5)
cv2.putText(res, 'Line', (300, 520), fontFace=cv2.FONT_ITALIC,fontScale=0.9, color=(0, 0, 0), thickness=3)
cv2.rectangle(res, (100, 100), (300, 200), (255, 0, 139), 5)
cv2.putText(res, 'Rectangle', (100, 90), fontFace=cv2.FONT_ITALIC,fontScale=0.9, color=(0, 0, 0), thickness=3)
cv2.circle(res, (800, 550), 100, (0, 0, 255), 5)
cv2.putText(res, 'Circle', (650, 650), fontFace=cv2.FONT_ITALIC, fontScale=0.9, color=(0, 0, 0), thickness=3)
cv2.imshow("IMG", res)
cv2.waitKey(0)
cv2.destroyAllWindows()