import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def regresion_multiple_comparar(X, y, modelos):
    """
    Ajusta varios modelos de regresión múltiple y compara R².
    X: DataFrame con todas las variables predictoras
    y: Serie o array con la variable respuesta
    """
    resultados = {}
    
    for i, variables in enumerate(modelos, start=1):
        X_sel = X[variables]
        modelo = LinearRegression()
        modelo.fit(X_sel, y)
        
        beta0 = modelo.intercept_
        betas = modelo.coef_
        y_pred = modelo.predict(X_sel)
        r2 = r2_score(y, y_pred)
        
        print(f"\nModelo {i}: Variables = {variables}")
        print(f"β0 (intercepto) = {beta0:.4f}")
        for var, b in zip(variables, betas):
            print(f"β_{var} = {b:.4f}")
        print(f"R² = {r2:.4f}")
        
        resultados[f"Modelo {i}"] = {
            "variables": variables,
            "beta0": beta0,
            "betas": dict(zip(variables, betas)),
            "R2": r2
        }
    
    return resultados

# Ejemplo
datos = {
    "Horas_estudio": [2, 4, 6, 8, 10, 12, 14, 16],
    "Asistencia": [80, 82, 85, 88, 90, 92, 95, 97],
    "Practicas": [3, 4, 4, 5, 6, 6, 7, 8],
    "Puntaje": [60, 65, 70, 72, 75, 78, 82, 85]
}
df = pd.DataFrame(datos)

# Lista de modelos a probar
modelos_a_probar = [
    ["Horas_estudio"],  # Modelo simple
    ["Horas_estudio", "Asistencia"],  # Modelo con 2 predictores
    ["Horas_estudio", "Asistencia", "Practicas"]  # Modelo con 3 predictores
]

# Comparación de modelos
resultados = regresion_multiple_comparar(
    X=df[["Horas_estudio", "Asistencia", "Practicas"]],
    y=df["Puntaje"],
    modelos=modelos_a_probar
)