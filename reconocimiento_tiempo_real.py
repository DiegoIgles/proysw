import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Cargar el modelo de detección de objetos
modelo_objeto = tf.keras.models.load_model('modelo_objeto.h5')

# Cargar el modelo de detección de anomalías sin compilar y luego compilar
autoencoder = tf.keras.models.load_model('autoencoder_model.h5', compile=False)
autoencoder.compile(optimizer='adam', loss='mse')

def real_time_detection():
    cap = cv2.VideoCapture(0)
    anomaly_threshold = 0.0107  # AJUSTAR ESTE VALOR A UN VALOR CERCANO AL QUE APARECE CUANDO EJECUTAS EL COMANDO DE RECONOCIMIENTO EN TIEMPO REAL, UN VALOR CERCANO AL ERROR DE RECONSTRUCCION
    object_threshold = 0.2    # Umbral para detección de objeto

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Procesamiento de la imagen para los modelos
        img = cv2.resize(frame, (224, 224))
        img_norm = img / 255.0
        img_norm_expanded = np.expand_dims(img_norm, axis=0)

        # Predicción para detección de objeto
        prediction = modelo_objeto.predict(img_norm_expanded)
        prediction_value = prediction[0][0]
        print(f"Predicción de objeto: {prediction_value}")

        # Predicción para detección de anomalías
        reconstructed = autoencoder.predict(img_norm_expanded)
        error = np.mean(np.square(img_norm_expanded - reconstructed))
        print(f"Error de reconstrucción: {error}")

        # Decidir etiquetas y colores basados en las predicciones
        # Detección de objeto
        if prediction_value > object_threshold:
            obj_label = "Objeto detectado"
            obj_color = (0, 255, 0)  # Verde
            # Dibujar rectángulo alrededor del objeto (ajusta las coordenadas según sea necesario)
            cv2.rectangle(frame, (50, 50), (frame.shape[1]-50, frame.shape[0]-50), obj_color, 2)
        else:
            obj_label = "Objeto no detectado"
            obj_color = (0, 0, 255)  # Rojo

        # Detección de anomalías
        if error > anomaly_threshold:
            anomaly_label = "Anomalia detectada"
            anomaly_color = (0, 0, 255)  # Rojo
        else:
            anomaly_label = "Normal"
            anomaly_color = (0, 255, 0)  # Verde

        # Mostrar las etiquetas en la imagen
        cv2.putText(frame, obj_label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, obj_color, 2)
        cv2.putText(frame, anomaly_label, (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, anomaly_color, 2)

        cv2.imshow('Detección en Tiempo Real', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    real_time_detection()