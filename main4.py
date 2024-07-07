import cv2
import numpy as np

image1= cv2.imread("input2.png")

cv2.imshow("Orignal", image1)

kernel=np.ones((5,5), np.uint8)
erosion = cv2.erode(image1,kernel)
cv2.imshow("output", erosion )
cv2.waitKey(0)
cv2.destroyAllWindows()