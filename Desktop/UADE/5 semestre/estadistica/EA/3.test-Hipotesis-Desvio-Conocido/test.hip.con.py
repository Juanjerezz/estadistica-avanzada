from scipy.stats import norm
import math

def test_hipotesis_media_sigma_conocido(x_bar, mu_0, sigma, n, alpha=0.05, tipo='bilateral'):
    z = (x_bar - mu_0) / (sigma / math.sqrt(n))

    if tipo == 'bilateral':
        z_critico = norm.ppf(1 - alpha / 2)
        p_value = 2 * (1 - norm.cdf(abs(z)))
        rechazo = abs(z) > z_critico

    elif tipo == 'derecha':
        z_critico = norm.ppf(1 - alpha)
        p_value = 1 - norm.cdf(z)
        rechazo = z > z_critico

    elif tipo == 'izquierda':
        z_critico = norm.ppf(alpha)
        p_value = norm.cdf(z)
        rechazo = z < z_critico

    else:
        raise ValueError("Tipo debe ser 'bilateral', 'derecha' o 'izquierda'.")

    return {
        'z': round(z, 4),
        'z_critico': round(z_critico, 4),
        'p_value': round(p_value, 4),
        'rechazar_H0': rechazo
    }

def calcular_tamanio_muestra_sigma_conocido(delta, sigma, alpha, beta, tipo_test='bilateral'):
    if tipo_test == 'bilateral':
        z_alpha = norm.ppf(1 - alpha / 2)
    else:
        z_alpha = norm.ppf(1 - alpha)

    z_beta = norm.ppf(1 - beta)

    n = ((z_alpha + z_beta) * sigma / delta) ** 2
    return math.ceil(n)


#uso
resultado = test_hipotesis_media_sigma_conocido(
    x_bar=92,
    mu_0=90,
    sigma=3,
    n=30,
    alpha=0.05,
    tipo='bilateral'  # Puede ser 'bilateral', 'izquierda', o 'derecha'
)

print("Resultado del test:")
for clave, valor in resultado.items():
    print(f"{clave}: {valor}")


#uso cuando pide tamaño de muestra 
delta = 2 # Diferencia mínima a detectar
sigma = 4  # Desvío estándar conocido
alpha = 0.05 # Nivel de significancia (5%)
beta = 0.2 # Error tipo II 

n = calcular_tamanio_muestra_sigma_conocido(delta, sigma, alpha, beta, tipo_test='bilateral')
print(f"Tamaño de muestra necesario: {n}")
