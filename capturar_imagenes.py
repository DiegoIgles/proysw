import cv2
import os

def capture_images(label, num_images=50, save_dir="imagenes"):
    # Verifica si el directorio existe y, si no, lo crea
    if not os.path.exists(save_dir):
        try:
            os.makedirs(save_dir)
            print(f"Directorio creado: {save_dir}")
        except Exception as e:
            print(f"Error al crear el directorio: {e}")
            return
    
    cap = cv2.VideoCapture(0)
    img_count = 0

    while img_count < num_images:
        ret, frame = cap.read()
        if not ret:
            print("No se pudo acceder a la cámara.")
            break

        cv2.imshow('Capture', frame)
        
        # Guardar la imagen
        img_name = f"{save_dir}/{label}_{img_count}.jpg"
        print(f"Guardando imagen: {img_name}")  # Añadimos impresión para ver la ruta de guardado
        
        success = cv2.imwrite(img_name, frame)
        if success:
            print(f"Imagen {img_name} guardada con éxito.")
        else:
            print(f"Error al guardar la imagen {img_name}.")
        
        img_count += 1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    label = input("Introduce 'objeto' para imágenes positivas, o 'no_objeto' para imágenes negativas: ")
    save_dir = input("Introduce la ruta de la carpeta para guardar las imágenes (o presiona Enter para usar la carpeta predeterminada 'imagenes'): ")
    
    if save_dir == "":
        save_dir = "imagenes"
    
    capture_images(label, save_dir=save_dir)

