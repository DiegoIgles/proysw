# Object Recognition System

Este proyecto permite capturar imágenes de objetos con OpenCV y reconocer los objetos usando TensorFlow y con un modelo entrenado por el usuario.

## Requisitos

- Python 3.x

## Instalación

Primero, instala las dependencias:

```bash
pip install -r requirements.txt

## Inicializacion

Para iniciar el proyecto ejecutar estos comandos:

Para crear las imagenes:

python capturar_imagenes.py

poner objeto para imagenes positivas y no_objeto para imagenes negativas

Para entrenar el modelo:

python entrenar_modelo.py

Para iniciar el reconocimiento:

python reconocimiento_tiempo_real.py