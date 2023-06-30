# Imagen base de Python con Jupyter Notebook
FROM jupyter/scipy-notebook

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos del proyecto al contenedor
COPY My_notebook.ipynb .
COPY main.py .
COPY requirements.txt .

# Instalar las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Ejecutar el notebook y generar el modelo y el scaler
RUN jupyter nbconvert --to python My_notebook.ipynb 
RUN python My_notebook.py

# Comando para ejecutar el script de predicciones
CMD ["python", "main.py"]
