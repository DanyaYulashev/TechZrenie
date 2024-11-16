import cv2, numpy as np
res = np.full((400, 150, 3), (255/255, 255/255, 255/255))
for j in range(0, 151, 20):
    for i in range(0, 401, 20):
        cv2.rectangle(res, (j, i), (j+10, i+10), (255/255, 0/255, 139/255), -1)
for j in range(10, 151, 20):
    for i in range(10, 401, 20):
        cv2.rectangle(res, (j, i), (j+10, i+10), (255/255, 0/255, 139/255), -1)
cv2.imshow("IMG", res)
cv2.waitKey(5000)
cv2.destroyAllWindows()