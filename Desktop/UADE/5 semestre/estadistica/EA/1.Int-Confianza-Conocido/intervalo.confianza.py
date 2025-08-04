import math
from scipy.stats import norm

def intervalo_confianza_media(x_bar, sigma, n, confianza=0.95):
    alpha = 1 - confianza
    z = norm.ppf(1 - alpha/2) #distribucion normal estandar 
    error_estandar = sigma / math.sqrt(n)
    
    li = x_bar - z * error_estandar
    ls = x_bar + z * error_estandar

    error_muestreo= z * error_estandar
    
    return (round(li,4), round(ls,4)), round(error_muestreo,4)

def calcular_tamano_muestra(sigma, error_muestreo, confianza=0.95):
    alpha = 1 - confianza
    z = norm.ppf(1 - alpha/2)
    n = (z * sigma / error_muestreo) ** 2
    return math.ceil(n)  # redondeo hacia arriba

# uso
resultado,error_muestreo = intervalo_confianza_media(x_bar=92, sigma=3, n=6, confianza=0.95)
print(f"Intervalo de confianza: {resultado}")
print(f"Error de muestreo: {error_muestreo}")

#uso cuando pide tamaño de n que el error 
sigma = 3
error_deseado = 2.4004/2 #aca ingreso el que me pida ej, /2 si me pide la mitad del error anterior
confianza = 0.95

n_requerido = calcular_tamano_muestra(sigma, error_deseado, confianza)
print(f"Tamaño de muestra necesario: {n_requerido}")