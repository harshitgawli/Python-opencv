import cv2

path = "C:/Users/harsh/OneDrive/Desktop/test pics/itachi_4.jpg"

img = cv2.imread(path,1)

if img is None :
    print("Image load fail. wrong path")
else:
    cv2.namedWindow("frame",cv2.WINDOW_NORMAL)
    cv2.resizeWindow("frame",600,600)
    img= cv2.line(img,(10,20),(600,800),(0,255,0),15)
    img = cv2.arrowedLine(img, (50,50),(100,1200),(255,0,0),20)
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img,'harshit',(1080,1040),font,10,(0,0,255),20,cv2.LINE_AA)
    # img = cv2.flip(img,1)
    img = cv2.rectangle(img,(500,500),(1200,1500),(0,255,0),60)
    cv2.imshow("frame",img)
    cv2.waitKey(0)
    

cv2.destroyAllWindows()
    
