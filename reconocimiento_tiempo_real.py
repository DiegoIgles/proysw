import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Cargar el modelo de detección de objetos
modelo_objeto = tf.keras.models.load_model('modelo_objeto.h5')

# Cargar el modelo de detección de anomalías sin compilar y luego compilar
autoencoder = tf.keras.models.load_model('autoencoder_model.h5', compile=False)
autoencoder.compile(optimizer='adam', loss='mse')
                                              #estos dos se pueden modificar a gusto
def ajustar_umbral_anomalia(prediction_value, min_threshold=0.001, max_threshold=0.005):
    """
    Ajusta el umbral de anomalía basado en el valor de predicción.

    :param prediction_value: Valor de predicción del modelo de detección de objetos (0 a 1).
    :param min_threshold: Umbral mínimo de anomalía.
    :param max_threshold: Umbral máximo de anomalía.
    :return: Umbral de anomalía ajustado.
    """
    # Asegurar que prediction_value esté entre 0 y 1
    prediction_value = np.clip(prediction_value, 0, 1)
    
    # Calcular el umbral de anomalía directamente proporcional al prediction_value (lo que está en parentesis se puede modificar a gusto)
    anomaly_threshold = min_threshold + ((prediction_value-(prediction_value*0.01)) * (max_threshold - (min_threshold+0.0005)))
    
    return anomaly_threshold

def real_time_detection():
    cap = cv2.VideoCapture(0)
    base_anomaly_threshold = 0.005  # Umbral base para anomalías
    base_object_threshold = 0.5       # Umbral base para detección de objeto, se puede modificar a gusto

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

        # Ajustar el umbral de anomalía basado en prediction_value
        anomaly_threshold = ajustar_umbral_anomalia(prediction_value)
        print(f"Umbral de anomalía ajustado: {anomaly_threshold}")

        # Predicción para detección de anomalías
        reconstructed = autoencoder.predict(img_norm_expanded)
        error = np.mean(np.square(img_norm_expanded - reconstructed))
        print(f"Error de reconstrucción: {error}")

        # Decidir etiquetas y colores basados en las predicciones
        # Detección de objeto
        if prediction_value > base_object_threshold:
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
