import cv2

def face_detection(frame):
    face_classifier = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    # ora applichiamo il classificatore alla nostra immagine
    face = face_classifier.detectMultiScale(
        frame, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
    )

    
    faces_area = []
    for (x, y, w, h) in face:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 4)
        face_surface = frame[y+5:y + h-5, x+5:x + w-5]
        resized_image = cv2.resize(face_surface,(224,224), interpolation= cv2.INTER_AREA)
        faces_area.append(resized_image)
        
    return faces_area, face