import cv2

from ffpyplayer.player import MediaPlayer
path = "C:/Users/harsh/OneDrive/Desktop/test pics/Why_this_kolaveri.mp4"

cap = cv2.VideoCapture(path)
voice = MediaPlayer(path)
cv2.namedWindow("image",cv2.WINDOW_NORMAL)
cv2.resizeWindow("image",900,650)
while(cap.isOpened()):
    ret, frame = cap.read()
    audio_frame = voice.get_frame()
    print((cap.get(cv2.CAP_PROP_POS_MSEC))/1000)
    cv2.imshow("image",frame)


    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()