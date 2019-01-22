import imutils
import cv2
image = cv2.imread("nature.jpeg")
(h, w, d) = image.shape
cv2.imshow("Image", image)
cv2.imwrite('Home/img/Original.png',image)
cv2.waitKey(0)

#Anticlockwise rotation
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, 45, 1.0)
Arotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Anticlockwise Rotation", Arotated)
cv2.imwrite('Home/img/Arotated.png',Arotated)
cv2.waitKey(0)

# Clockwise Rotation
rotated = imutils.rotate(image, -45)
cv2.imshow("Clockwise Rotation", rotated)
cv2.imwrite('Home/img/rotated.png',rotated)
cv2.waitKey(0)
# cv2.imwrite('Roated.png',rotated)

#Invereted
Invereted = imutils.rotate(image, 180)
cv2.imshow("Invereted", Invereted)
cv2.imwrite('Home/img/Invereted.png',Invereted)
cv2.waitKey(0)

#Black and White
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image",gray_image)
cv2.imwrite('Home/img/gray_image.png',gray_image)
cv2.waitKey(0)

#Blurred
blurred = cv2.GaussianBlur(image, (11, 11), 0)
cv2.imshow("Blurred", blurred)
cv2.imwrite('Home/img/blurred.png',blurred)
cv2.waitKey(0)

#More Blurred
Mblurred = cv2.GaussianBlur(image, (111, 111), 0)
cv2.imshow("More Blurred", Mblurred)
cv2.imwrite('Home/img/Mblurred.png',Mblurred )
cv2.waitKey(0)

#Bounding Boxes
output =  imutils.rotate(image, 90) 
cv2.imshow("Bounding Boxes", output)
cv2.imwrite('Home/img/output.png',output)
cv2.waitKey(0)

#Outlines
Outlines = cv2.Canny(gray_image, 30, 150)
cv2.imshow("Edged", Outlines)
cv2.imwrite('Home/img/Outlines.png',Outlines )
cv2.waitKey(0)
