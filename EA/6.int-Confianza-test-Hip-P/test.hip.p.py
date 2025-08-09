import math
from scipy.stats import norm

def test_hipotesis_proporcion(x, n, p0, alpha=0.05, tipo='bilateral'):
    p_hat = x / n
    error_std = math.sqrt(p0 * (1 - p0) / n)
    z_stat = (p_hat - p0) / error_std

    if tipo == 'bilateral':
        z_critico = norm.ppf(1 - alpha / 2)
        p_value = 2 * (1 - norm.cdf(abs(z_stat)))
        rechazo = abs(z_stat) > z_critico

        p_hat_critico_izq = p0 - z_critico * error_std
        p_hat_critico_der = p0 + z_critico * error_std

        return {
            'p_hat': round(p_hat, 4),
            'z': round(z_stat, 4),
            'z_critico': round(z_critico, 4),
            'p_value': round(p_value, 4),
            'p_hat_critico_izquierda': round(p_hat_critico_izq, 4),
            'p_hat_critico_derecha': round(p_hat_critico_der, 4),
            'rechazar_H0': rechazo
        }

    elif tipo == 'derecha':
        z_critico = norm.ppf(1 - alpha)
        p_value = 1 - norm.cdf(z_stat)
        rechazo = z_stat > z_critico

        p_hat_critico = p0 + z_critico * error_std

        return {
            'p_hat': round(p_hat, 4),
            'z': round(z_stat, 4),
            'z_critico': round(z_critico, 4),
            'p_value': round(p_value, 4),
            'p_hat_critico': round(p_hat_critico, 4),
            'rechazar_H0': rechazo
        }

    elif tipo == 'izquierda':
        z_critico = norm.ppf(alpha)
        p_value = norm.cdf(z_stat)
        rechazo = z_stat < z_critico

        p_hat_critico = p0 + z_critico * error_std  

        return {
            'p_hat': round(p_hat, 4),
            'z': round(z_stat, 4),
            'z_critico': round(z_critico, 4),
            'p_value': round(p_value, 4),
            'p_hat_critico': round(p_hat_critico, 4),
            'rechazar_H0': rechazo
        }

    else:
        raise ValueError("Tipo debe ser 'bilateral', 'derecha' o 'izquierda'.")


resultado = test_hipotesis_proporcion(
    x=25,         # cantidad de éxitos
    n=30,         # tamaño muestral
    p0=0.7,       # proporción bajo H0
    alpha=0.05,
    tipo='derecha'
)

print("Resultado del test para la proporción:")
for clave, valor in resultado.items():
    print(f"{clave}: {valor}")