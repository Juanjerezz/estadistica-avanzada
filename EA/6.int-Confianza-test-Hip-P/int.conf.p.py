import math
from scipy.stats import norm

def intervalo_confianza_proporcion(x, n, confianza=0.95):
    p_hat = x / n #x cant de exitos
    z = norm.ppf(1 - (1 - confianza) / 2)
    error = z * math.sqrt(p_hat * (1 - p_hat) / n)
    
    li = p_hat - error
    ls = p_hat + error
    return (round(li, 4), round(ls, 4)), round(error, 4)



intervalo, error = intervalo_confianza_proporcion(x=150, n=600, confianza=0.90)

print("Intervalo de confianza para la varianza:", intervalo)
print("Error de muestreo:", error)