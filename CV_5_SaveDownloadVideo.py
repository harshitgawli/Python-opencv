import cv2
from ffpyplayer.player import MediaPlayer

path = "C:/Users/harsh/OneDrive/Desktop/test pics/Why_this_kolaveri.mp4"

cap = cv2.VideoCapture(path)
four_cc = cv2.VideoWriter.fourcc(*"XVID")

out = cv2.VideoWriter("pyCam2.mp4",four_cc,20.0,(640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if(ret == True):
        out.write(frame)
        cv2.imshow("Capturing",frame)
        if (cv2.waitKey(20)==ord('q')):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()