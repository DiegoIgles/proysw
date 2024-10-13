import cv2
import numpy as np
import tensorflow as tf
model = tf.keras.models.load_model('modelo_objeto.h5')

def real_time_object_recognition():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        img = cv2.resize(frame, (224, 224)) 
        img = img / 255.0  
        img = np.expand_dims(img, axis=0) 

        prediction = model.predict(img)

        if prediction > 0.5:  
            label = "Objeto detectado"
            color = (0, 255, 0) 

            cv2.putText(frame, label, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2, cv2.LINE_AA)
            cv2.rectangle(frame, (100, 100), (500, 500), color, 2)
        
        cv2.imshow('Reconocimiento', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    real_time_object_recognition()
