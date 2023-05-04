import numpy as np
import cv2
import time
import os

# Label: 00000 is not holding money, or ilegal money. 
# The rest is value of Vietnam's polymer money
label = "00000"

cap = cv2.VideoCapture(0)

i=0
while(True):
    i+=1
    ret, frame = cap.read()
    if not ret:
        continue
    frame = cv2.resize(frame, dsize=None,fx=0.3,fy=0.3)

    # Show
    cv2.imshow('frame',frame)

    # Save data
    if i>=60 and i%5==0 :
        print("Số ảnh capture = ",i-60)
        # create folder if not have yet
        if not os.path.exists('data/' + str(label)):
            os.mkdir('data/' + str(label))

        cv2.imwrite('data/' + str(label) + "/" + str(i) + ".png",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()