import cv2
path = "C:/Users/harsh/OneDrive/Desktop/test pics/itachi_1.png"
img = cv2.imread(path,1)

if img is None:
    print("Error: Unable to load image. Please check the file path.")
else:
    cv2.namedWindow("image",cv2.WINDOW_NORMAL)
cv2.resizeWindow("image",600,600)
cv2.imshow("image",img)
cv2.waitKey(0)

cv2.destroyAllWindows()