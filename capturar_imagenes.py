import cv2
import os

def capture_images(label, num_images=50, save_dir="imagenes"):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    cap = cv2.VideoCapture(0)
    img_count = 0

    while img_count < num_images:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow('Capture', frame)
        
        # Guardar la imagen
        img_name = f"{save_dir}/{label}_{img_count}.jpg"
        cv2.imwrite(img_name, frame)
        print(f"Imagen {img_name} capturada.")
        img_count += 1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    label = input("Introduce 'objeto' para imágenes positivas, o 'no_objeto' para imágenes negativas: ")
    capture_images(label)
