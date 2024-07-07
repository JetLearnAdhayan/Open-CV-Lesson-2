import cv2

image1 = cv2.imread("input2.png")

cv2.imshow("orignal", image1)

Gausian = cv2.GaussianBlur(image1,(7,7),0)
cv2.imshow("gausian blurring", Gausian)

Median = cv2.medianBlur(image1,5)
cv2.imshow("Median Blur", Median)

billateral = (cv2.bilateralFilter(image1,9,75,75))
cv2.imshow("billateral blurring", billateral)









cv2.waitKey(0)
cv2.destroyAllWindows()

# Gaussian Blur - used mostly in machine learning preprocessing steps
#Gaussian blur describes blurring an image by a Gaussian function. 
#It is a widely used effect in graphics software, typically to reduce image noise and reduce detail.
#(img, Kernal_size ,std_dev)
# Median Blur -widely used in digital image processing because, under certain conditions, 
# it preserves edges while removing noise.
#(img,Kernal_size)
# Bilateral Blur - only sharp edges are preserved here
#(img,diameter of each pixel neighborhood,sigmaColor,sigmaSpace)