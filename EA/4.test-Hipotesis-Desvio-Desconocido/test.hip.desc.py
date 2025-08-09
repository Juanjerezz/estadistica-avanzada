import math
from scipy.stats import t

def test_hipotesis_media_sigma_desconocido(x_bar, mu_0, s, n, alpha=0.05, tipo='bilateral'):
    gl = n - 1  #grados de libertad
    t_stat = (x_bar - mu_0) / (s / math.sqrt(n))

    if tipo == 'bilateral':
        t_critico = t.ppf(1 - alpha / 2, df=gl)
        p_value = 2 * (1 - t.cdf(abs(t_stat), df=gl))
        rechazo = abs(t_stat) > t_critico

    elif tipo == 'derecha':
        t_critico = t.ppf(1 - alpha, df=gl)
        p_value = 1 - t.cdf(t_stat, df=gl)
        rechazo = t_stat > t_critico

    elif tipo == 'izquierda':
        t_critico = t.ppf(alpha, df=gl)
        p_value = t.cdf(t_stat, df=gl)
        rechazo = t_stat < t_critico

    else:
        raise ValueError("Tipo debe ser 'bilateral', 'derecha' o 'izquierda'.")

    return {
        't': round(t_stat, 4),
        't_critico': round(t_critico, 4),
        'p_value': round(p_value, 4),
        'rechazar_H0': rechazo
    }

#uso
resultado = test_hipotesis_media_sigma_desconocido(
    x_bar=50,
    mu_0=55,
    s=10, #desvio estandar muestral
    n=25,
    alpha=0.05,
    tipo='bilateral'
)

print("Resultado del test:")
for clave, valor in resultado.items():
    print(f"{clave}: {valor}")