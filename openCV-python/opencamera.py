# เปิดกล้อง
import cv2
import datetime

cap = cv2.VideoCapture(0)

while (cap.isOpened()):
    result, frame = cap.read()

    curdate = str(datetime.datetime.now())
    cv2.putText(frame, curdate, (100, 40), cv2.FONT_HERSHEY_COMPLEX, 1.5, (0, 0, 255), 4, cv2.LINE_4)
    cv2.imshow('out', frame)
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

cap.release()
cv2.destroyAllWindows()