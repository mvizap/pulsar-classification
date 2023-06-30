import argparse
import pickle
import numpy as np

# Parsear los argumentos de línea de comandos
parser = argparse.ArgumentParser()
parser.add_argument('--Mean_Integrated', type=float, required=True)
parser.add_argument('--SD', type=float, required=True)
parser.add_argument('--EK', type=float, required=True)
parser.add_argument('--Skewness', type=float, required=True)
parser.add_argument('--Mean_DMSNR_Curve', type=float, required=True)
parser.add_argument('--SD_DMSNR_Curve', type=float, required=True)
parser.add_argument('--EK_DMSNR_Curve', type=float, required=True)
parser.add_argument('--Skewness_DMSNR_Curve', type=float, required=True)
args = parser.parse_args()

# Cargar el modelo desde el archivo
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Cargar el scaler desde el archivo
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# Función para realizar predicciones
def predict(model, scaler, values):
    # Escalar los valores proporcionados
    scaled_values = scaler.transform([values])
    # Realizar la predicción utilizando el modelo cargado
    prediction = model.predict(scaled_values)
    return prediction

# Valores proporcionados como argumentos de línea de comandos
values = [args.Mean_Integrated, args.SD, args.EK, args.Skewness, args.Mean_DMSNR_Curve, args.SD_DMSNR_Curve, args.EK_DMSNR_Curve, args.Skewness_DMSNR_Curve]

# Realizar la predicción
prediction = predict(model, scaler, values)

# Imprimir el resultado de la predicción
print("Prediction:", prediction)
