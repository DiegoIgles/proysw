import os
import cv2
import numpy as np

def load_images(image_folder, img_size=(224, 224)):
    images = []
    labels = []
    for filename in os.listdir(image_folder):
        if filename.endswith(".jpg"):
            img = cv2.imread(os.path.join(image_folder, filename))
            img = cv2.resize(img, img_size)  
            img = img / 255.0 
            images.append(img)

            if "no_objeto" in filename:
                labels.append(0)
            elif "objeto" in filename:
                labels.append(1)
            else:
                print(f"Nombre de archivo desconocido: {filename}")
                continue
            

    return np.array(images), np.array(labels)
