import cv2 
img = cv2.imread(r"C:\Users\GURRAMKONDAMEENAZ\Pictures\MEENAZ 98.jpg") 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
cv2.CascadeClassifier(r"C:\Users\GURRAMKONDAMEENAZ\Pictures\MEENAZ 98.jpg") 
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5) 
for (x, y, w, h) in faces: 
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2) 
cv2.imshow('Faces Detected', img) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 
