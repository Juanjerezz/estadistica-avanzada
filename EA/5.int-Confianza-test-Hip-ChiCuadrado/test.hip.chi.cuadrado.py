import math
from scipy.stats import chi2

def test_hipotesis_varianza(s, sigma_0, n, alpha=0.05, tipo='bilateral'):
    gl = n - 1
    s2 = s ** 2
    sigma2_0 = sigma_0 ** 2
    chi2_stat = (gl * s2) / sigma2_0

    if tipo == 'bilateral':
        chi2_crit_izq = chi2.ppf(alpha / 2, df=gl)
        chi2_crit_der = chi2.ppf(1 - alpha / 2, df=gl)
        p_value = 2 * min(chi2.cdf(chi2_stat, df=gl), 1 - chi2.cdf(chi2_stat, df=gl))
        rechazo = chi2_stat < chi2_crit_izq or chi2_stat > chi2_crit_der

        return {
            'chi2': round(chi2_stat, 4),
            'chi2_critico_izquierdo': round(chi2_crit_izq, 4),
            'chi2_critico_derecho': round(chi2_crit_der, 4),
            'p_value': round(p_value, 4),
            'rechazar_H0': rechazo
        }

    elif tipo == 'derecha':
        chi2_crit = chi2.ppf(1 - alpha, df=gl)
        p_value = 1 - chi2.cdf(chi2_stat, df=gl)
        rechazo = chi2_stat > chi2_crit

    elif tipo == 'izquierda':
        chi2_crit = chi2.ppf(alpha, df=gl)
        p_value = chi2.cdf(chi2_stat, df=gl)
        rechazo = chi2_stat < chi2_crit

    else:
        raise ValueError("Tipo debe ser 'bilateral', 'derecha' o 'izquierda'.")

    return {
        'chi2': round(chi2_stat, 4),
        'chi2_critico': round(chi2_crit, 4),
        'p_value': round(p_value, 4),
        'rechazar_H0': rechazo
    }


resultado = test_hipotesis_varianza(
    s=18.2,          # Desvío estándar muestral
    sigma_0=15,    # Desvío estándar poblacional bajo H0
    n=10,         # Tamaño de muestra
    alpha=0.05,
    tipo='derecha'
)

print("Resultado del test para la varianza:")
for clave, valor in resultado.items():
    print(f"{clave}: {valor}")