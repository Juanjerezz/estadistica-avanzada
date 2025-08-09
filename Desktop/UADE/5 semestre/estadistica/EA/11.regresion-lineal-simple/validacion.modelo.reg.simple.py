import numpy as np
import math
from scipy import stats

def validar_modelo_regresion(x, y, confianza=0.95):
    """
    Valida un modelo de regresión lineal simple con pasos:
    1) R2 >= 0.5 para aceptar modelo
    2) Análisis de coeficiente de correlación (>=0.7 intenso, <0.7 débil)
    3) Test de hipótesis para pendiente del modelo
    """
    x = np.array(x)
    y = np.array(y)
    n = len(x)

    # Ajuste
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    Sxx = np.sum((x - x_mean)**2)
    Sxy = np.sum((x - x_mean)*(y - y_mean))
    beta1 = Sxy / Sxx
    beta0 = y_mean - beta1 * x_mean
    y_pred = beta0 + beta1 * x

    # R2
    ss_tot = np.sum((y - y_mean)**2)
    ss_res = np.sum((y - y_pred)**2)
    R2 = 1 - (ss_res / ss_tot)

    # Correlación
    r_num = Sxy
    r_den = math.sqrt(Sxx * np.sum((y - y_mean)**2))
    r = r_num / r_den

    # Test hipótesis pendiente
    residuos = y - y_pred
    s2 = np.sum(residuos**2) / (n - 2)
    s = math.sqrt(s2)
    se_beta1 = s / math.sqrt(Sxx)
    t_stat = beta1 / se_beta1
    df = n - 2
    p_valor = 2 * (1 - stats.t.cdf(abs(t_stat), df))

    # Intervalo confianza beta1
    t_crit = stats.t.ppf(1 - (1 - confianza) / 2, df)
    ci_beta1 = (beta1 - t_crit * se_beta1, beta1 + t_crit * se_beta1)

    print(f"Coeficiente de determinación R² = {R2:.3f}")
    if R2 < 0.5:
        print("=> R² menor a 0.5, se descarta el modelo por baja capacidad explicativa.")
    else:
        print("=> R² es aceptable, el modelo explica una buena parte de la variabilidad.")

    print(f"\nCoeficiente de correlación r = {r:.3f}")
    if abs(r) >= 0.7:
        print("=> Existe una relación intensa entre X e Y.")
    else:
        print("=> La relación entre X e Y es débil.")

    print(f"\nTest de hipótesis para pendiente β1:")
    print(f"t estadístico = {t_stat:.3f}, p-valor = {p_valor:.4f}")
    if p_valor < (1 - confianza):
        print("=> Rechazamos H0: la pendiente es significativa.")
    else:
        print("=> No se rechaza H0: no hay evidencia suficiente para afirmar que la pendiente es distinta de cero.")

    return {
        "R2": R2,
        "r": r,
        "beta0": beta0,
        "beta1": beta1,
        "t_stat_beta1": t_stat,
        "p_valor_beta1": p_valor,
        "intervalo_confianza_beta1": ci_beta1
    }


# Ejemplo
x = [1,2,3,4,5,6,7,8,9]
y = [52,56,61,66,71,75,80,85,88]

resultado = validar_modelo_regresion(x, y)