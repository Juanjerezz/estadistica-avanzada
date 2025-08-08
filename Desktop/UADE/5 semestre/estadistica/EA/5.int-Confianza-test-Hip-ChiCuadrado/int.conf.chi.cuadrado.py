import math
from scipy.stats import chi2

def intervalo_confianza_varianza(s, n, confianza=0.95):
    alpha = 1 - confianza
    gl = n - 1  # grados de libertad

    chi2_inf = chi2.ppf(alpha / 2, gl)
    chi2_sup = chi2.ppf(1 - alpha / 2, gl)

    li = (gl * s**2) / chi2_sup
    ls = (gl * s**2) / chi2_inf

    error_muestreo = ls - li

    return (round(li, 4), round(ls, 4)), round(error_muestreo, 4)

intervalo, error = intervalo_confianza_varianza(s=4.2, n=25, confianza=0.95)

print("Intervalo de confianza para la varianza:", intervalo)
print("Error de muestreo:", error)