import cv2

face_data = cv2.CascadeClassifier('frontalface.xml')

## image to detect faces 
#img = cv2.imread('img_name.png')

## capture video from webcam 
video = cv2.VideoCapture(0)

while True:
    ## Read Frame
    frame_read, frame = video.read()

    ## convert to gray
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ## Detect coordinates (x, y, width, height)
    face_coordi = face_data.detectMultiScale(gray_img)

    ## To Draw rectangles  
    for (x, y, w, h) in face_coordi:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 225, 0), 3)
    
    ## To Display images
    cv2.imshow('Face Detection', frame)
    
    ## wait until press key
    key = cv2.waitKey(1)
    
    ## Press q or Q to stop
    if key ==81 or key ==113:
        break

print("Completed")
   






