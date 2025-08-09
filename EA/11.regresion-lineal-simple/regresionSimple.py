import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def regresion_lineal_simple(X, Y, mostrar_grafico=True):
    X = np.array(X).reshape(-1, 1)
    Y = np.array(Y)

    modelo = LinearRegression()
    modelo.fit(X, Y)

    beta0 = modelo.intercept_
    beta1 = modelo.coef_[0]
    Y_pred = modelo.predict(X)
    r2 = r2_score(Y, Y_pred)

    if mostrar_grafico:
        plt.scatter(X, Y, color="blue", label="Datos reales") #grafico de dispersion
        plt.plot(X, Y_pred, color="red", label=f"Recta ajustada: y = {beta0:.2f} + {beta1:.2f}x")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("Regresión Lineal Simple")
        plt.legend()
        plt.grid(True)
        plt.show()

    return {
        "beta0": beta0,
        "beta1": beta1,
        "R2": r2,
        "predicciones": Y_pred,
        "residuos": Y - Y_pred
    }

#ejemplo
horas = [1, 2, 3, 4, 5, 6, 7, 8, 9]
puntajes = [52, 56, 61, 66, 71, 75, 80, 85, 88]

resultado = regresion_lineal_simple(horas, puntajes) #x es la variable independiente(horas), y la dependiente(puntaje)

print(f"β0 (intercepto): {resultado['beta0']:.2f}")
print(f"β1 (pendiente): {resultado['beta1']:.2f}")
print(f"R²: {resultado['R2']:.3f}")