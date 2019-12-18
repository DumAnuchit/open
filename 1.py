import cv2
import time
import numpy as np
import csv

point1 = ()
point2 = ()
px1 = 0
px2 = 0
py1 = 0
py2 = 0
drawing = False


def mouse_drawing(event, x, y, flags, params):
    global point1, point2, drawing, px1, py1, px2, py2
    if event == cv2.EVENT_LBUTTONDOWN:
        if drawing is False:
            drawing = True
            point1 = (x, y)
            px1 = (x)
            py1 = (y)
        else:
            drawing = False

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing is True:
            point2 = (x, y)
            px2 = (x)
            py2 = (y)


cap = cv2.VideoCapture("1.mp4")

# ret, frame = cam.read()
#cv2.namedWindow("test")

img_counter = 0

while True:
    cv2.setMouseCallback("Image", mouse_drawing)

    print('px1: ', px1, ' py1: ', py1)
    print('px2: ', px2, ' py2: ', py2)

    ret, frame = cam.read()

    # cv2.rectangle(frame, (384, 0), (510, 128), (80,18,236), 2)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #cv2.imshow("test", frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

    if point1 and point2:
        try:
            print('                                                   ....')
            ret, frame = cam.read()
            cv2.rectangle(frame, point1, point2, (0, 0, 255))
            width = px2 - px1
            height = py2 - py1

            pixel = np.array(frame[py1:py2, px1:px2])
            # print('                     ......................  ',pixel)
            # Apply log transform. 
            c = 255 / (np.log(1 + np.max(pixel)))
            log_transformed = c * np.log(1 + pixel)
            # Specify the data type. 
            log_transformed = np.array(log_transformed, dtype=np.uint8)
            print('                     ......................  ', pixel)

            lines = cv2.HoughLinesP(frame[py1:py2, px1:px2], 1, np.pi / 180, 30, maxLineGap=250)

        except:
            pass

    cv2.imshow("Image", frame)
    k = cv2.waitKey(1)
    if k == 99:  # The press C is scan SD. Canny
        print('scan canny')

    if not ret:
        break

    if k % 256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break

cam.release()

cv2.destroyAllWindows()
