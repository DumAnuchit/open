import cv2
cap = cv2.VideoCapture("1.mp4")
while (True) :
        ret,frame = cap.read()
        cv2.imshow('frame',frame)
        img = cv.QueryFrame(cap)
        cv.Flip(img,img,1)
        x = 50
        y = 20
        w = 800
        h = 300
        subimg = cv.GetSubRect(img,(x,y,w,h))
        cv.ShowImage("subimg",subimg)
        if(cv2.waitKey(15) & 0xff==ord('a')):
           break
cap.release()
cv2.destroyAllWindows()