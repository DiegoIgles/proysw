import os
import numpy as np
import cv2
import tensorflow as tf

def load_normal_images(image_folder, img_size=(224, 224)):
    images = []
    for filename in os.listdir(image_folder):
        if filename.endswith(".jpg") and "objeto" in filename:
            img_path = os.path.join(image_folder, filename)
            img = cv2.imread(img_path)
            img = cv2.resize(img, img_size)
            img = img / 255.0
            images.append(img)
    return np.array(images)

# Cargar imágenes normales
X_train_normal = load_normal_images('./imagenes')

# Definir el autoencoder
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, UpSampling2D
from tensorflow.keras.models import Model

input_img = Input(shape=(224, 224, 3))

# Encoder
x = Conv2D(32, (3, 3), activation='relu', padding='same')(input_img)
x = MaxPooling2D((2, 2), padding='same')(x)
# Añade más capas según sea necesario

# Decoder
x = UpSampling2D((2, 2))(x)
x = Conv2D(3, (3, 3), activation='sigmoid', padding='same')(x)

autoencoder = Model(input_img, x)
autoencoder.compile(optimizer='adam', loss='mse')

# Entrenar el autoencoder
autoencoder.fit(X_train_normal, X_train_normal, epochs=50, batch_size=32, validation_split=0.1)

# Guardar el modelo
autoencoder.save('autoencoder_model.h5')
