import cv2
import sys

image_path = sys.argv[1]

image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=3,
        minSize=(30, 30)
)

print("Found {0} Faces!".format(len(faces)))

PADDING = 125

for (x, y, w, h) in faces:
    print(x, y, w, h)
    cv2.rectangle(image, (x-PADDING, y-PADDING), (x+w+PADDING, y+h+PADDING), (0, 255, 0), 2)

status = cv2.imwrite('faces_detected.jpg', image)
print("Image faces_detected.jpg written to filesystem: ",status)
