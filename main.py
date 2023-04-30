from ultralytics import YOLO
import math
import cv2 as cv
import time

# camera_number starts from 0. 1 is the second camera and so on. 
# if the camera is not available you will get an error
camera_number = 0 
cap = cv.VideoCapture(camera_number)

model = YOLO("AI_models/best.pt")  # loading the trained model that we got by going through the train.ipynb file.

classNames = ['Helmet', 'Goggles', 'Jacket', 'Gloves', 'Footwear'] #the classes in the data.yaml file

fps = 0
font = cv.FONT_HERSHEY_SIMPLEX

while True:
    start_time = time.time()

    success, img = cap.read()

    results = model(img, stream=True)

    #this loop will execute in every frame
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            cv.rectangle(img, (x1,y1),(x2,y2),(255,0,255),3)

            class_ids = box.cls[0]

            cv.putText(img,f"{classNames[int(class_ids)]}, {math.ceil((box.conf[0]*100))/100}",(x1,y1),font,1,(255,0,0),2)

            
            (x_center, y_center) = (x2 + x1)/2, (y2 + y1)/2
            cv.circle(img,(int(x_center),int(y_center)), 5, (0,0,255), -1)


    cv.putText(img,f"FPS: {fps:.2f}",(0,30),font,1,(255,0,0),2)
    cv.imshow("Test",img)

    if cv.waitKey(50) == 27:
        break

    fps = 1.0 / (time.time() - start_time)

