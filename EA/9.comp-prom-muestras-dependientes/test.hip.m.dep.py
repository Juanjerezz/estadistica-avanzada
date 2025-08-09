import math
from scipy.stats import t

def test_hipotesis_dependientes(datos1, datos2, mu_d0=0, alpha=0.05, tipo='bilateral'):
    if len(datos1) != len(datos2):
        raise ValueError("Las muestras deben tener el mismo tamaño.")

    diferencias = [x - y for x, y in zip(datos1, datos2)]
    n = len(diferencias)
    media_d = sum(diferencias) / n
    s_d = math.sqrt(sum((d - media_d)**2 for d in diferencias) / (n - 1))

    t_stat = (media_d - mu_d0) / (s_d / math.sqrt(n))

    if tipo == 'bilateral':
        t_critico = t.ppf(1 - alpha/2, df=n-1)
        rechazar = abs(t_stat) > t_critico
    elif tipo == 'cola_izq':
        t_critico = t.ppf(alpha, df=n-1)
        rechazar = t_stat < t_critico
    elif tipo == 'cola_der':
        t_critico = t.ppf(1 - alpha, df=n-1)
        rechazar = t_stat > t_critico
    else:
        raise ValueError("tipo debe ser 'bilateral', 'cola_izq' o 'cola_der'.")

    return {
        'media_diferencias': media_d,
        'desvio_diferencias': s_d,
        't_stat': t_stat,
        't_critico': t_critico,
        'rechazar_H0': rechazar
    }

#uso
antes = [85, 90, 88, 75, 95]
despues = [87, 92, 84, 78, 96]
resultado = test_hipotesis_dependientes(antes, despues, mu_d0=0, alpha=0.05, tipo='bilateral')
print(resultado)