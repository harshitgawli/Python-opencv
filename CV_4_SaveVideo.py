import cv2
# from ffpyplayer.player import MediaPlayer


cap = cv2.VideoCapture(0)
four_cc = cv2.VideoWriter.fourcc(*"XVID")

out = cv2.VideoWriter("pyCam3.mp4",four_cc,20.0,(640,480))

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