import cv2
import numpy as np

img = cv2.imread("colors.jpg")
rows, cols, _ = img.shape
print("Rows", rows)
print("Cols", cols)

# Cut image
cut_image = img[426: 526, 250: 1280]

# ROI (Region of interest)
cv2.rectangle(img, (385, 155), (851, 613), (0, 255, 0), 3)

roi = img[155: 613, 385: 851]

cv2.imshow("Cut image", cut_image)
cv2.imshow("Roi", roi)
cv2.imshow("image", img)
cv2.waitKey(0)