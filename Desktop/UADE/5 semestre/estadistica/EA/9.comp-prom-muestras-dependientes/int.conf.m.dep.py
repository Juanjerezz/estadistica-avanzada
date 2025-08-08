import math
from scipy.stats import t

def intervalo_confianza_dependientes(datos1, datos2, confianza=0.95):
    diferencias = [x - y for x, y in zip(datos1, datos2)]
    n = len(diferencias)
    media_d = sum(diferencias) / n
    s_d = math.sqrt(sum((d - media_d)**2 for d in diferencias) / (n - 1))

    t_critico = t.ppf(1 - (1 - confianza) / 2, df=n-1)

    error = t_critico * (s_d / math.sqrt(n))

    li = media_d - error
    ls = media_d + error
    return (round(li, 4), round(ls, 4)), round(error, 4)


#uso
antes = [85, 90, 88, 75, 95]
despues = [87, 92, 84, 78, 96]

intervalo, error = intervalo_confianza_dependientes(antes, despues, confianza=0.95)

print("Intervalo de confianza para la diferencia de medias (dependientes):", intervalo)
print("Error de muestreo:", error)