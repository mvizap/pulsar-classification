# Pulsar Project

Este proyecto contiene los siguientes archivos:

-  `My_notebook.ipynb`: Este notebook que analiza y realiza un modelo de predicción de estrellas pulsar. AL final, genera un modelo (`model.pkl`) y un escalador (`scaler.pkl`).

-  `main.py`: Este script utiliza el modelo y el escalador para hacer predicciones basadas en los valores proporcionados por el usuario.

- requeriments.txt

- Dockerfile: El archivo `Dockerfile` se encarga de construir una imagen de Docker basada en `jupyter/scipy-notebook`. El Dockerfile tiene la particularidad de convertir el notebook `My_notebook.ipynb` a un archivo `.py` y ejecutarlo para generar el modelo (`model.pkl`) y el escalador (`scaler.pkl`) automáticamente.


## Requisitos

  
Asegúrate de tener instaladas las siguientes dependencias:

- Docker

- Las bibliotecas especificadas en el archivo `Requirements.txt`


## Uso

1. Clona el repositorio ejecutando el siguiente comando:
   
```
   git clone https://github.com/mvizap/pulsar-classification.git
```

3. Ingresa a la carpeta con cd pulsar-classification (o el nombre que le hayas dado)
   
4. Construye la imagen de Docker ejecutando el siguiente comando en el directorio raíz del proyecto:

   ```

     docker build -t pulsar .
   ```


6. Ejecuta el contenedor de Docker utilizando el siguiente comando:
Este es un ejemplo de parametros. Tu puedes cambiar esto para que genere una predicción.
```
     docker run pulsar python main.py --Mean_Integrated 99.367188 --SD 41.572202 --EK 1.547197 --Skewness 4.154106 --Mean_DMSNR_Curve 27.555184 --SD_DMSNR_Curve 61.719016 --EK_DMSNR_Curve 2.208808 --Skewness_DMSNR_Curve 3.662680
```
