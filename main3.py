import cv2

image1 = cv2.imread("input1.png")

cv2.imshow("Orignal Image" ,image1)
resized = cv2.resize(image1, (500,250))
cv2.imshow("Output Image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()