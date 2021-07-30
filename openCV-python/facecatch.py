import cv2

img = cv2.imread('image.jpeg')

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

scaleFactor = 1.1
minNeighber = 3
face_detect = face_cascade.detectMultiScale(gray_img, scaleFactor, minNeighber)

for (x, y, w, h) in face_detect:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow('out', img)
cv2.waitKey(0)
cv2.destroyAllWindows()