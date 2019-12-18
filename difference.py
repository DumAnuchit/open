import cv2
import numpy as np

cap = cv2.VideoCapture("1.mp4")

_, first_frame = cap.read()
first_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
first_gray = cv2.GaussianBlur(first_gray, (5, 5), 0)
while True:
    _, frame = cap.read()
    x = 50
    y = 20
    w = 1000
    h = 500
    center_coordinates = (520, 500)
    radius = 20
    color = (255, 0, 0)
    thickness = 5
    position = cv2.boundingRect(first_gray)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)
    difference = cv2.absdiff(first_gray, gray_frame)
    img = cv2.circle(gray_frame, center_coordinates, radius, color, thickness)
    _, difference = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)
    crop = difference[y:y + h, x:x + w]
    cv2.imshow('Fra', crop)
    cv2.imshow("Frame", gray_frame)
    cv2.imshow("difference", img)

    if (cv2.waitKey(27) & 0xff == ord('a')):
        print(difference)
        break
cap.release()
cv2.destroyAllWindows()