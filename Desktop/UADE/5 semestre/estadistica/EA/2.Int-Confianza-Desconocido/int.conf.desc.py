import math
from scipy.stats import t

def intervalo_confianza_t(x_bar, s, n, confianza=0.95):
    alpha = 1 - confianza
    df = n - 1  # grados de libertad
    t_critico = t.ppf(1 - alpha/2, df) #aca uso la distribucion t-student
    error_estandar = s / math.sqrt(n)
    
    li = x_bar - t_critico * error_estandar
    ls = x_bar + t_critico * error_estandar
    
    error_muestreo = t_critico * error_estandar
    
    return (round(li,4), round(ls,4)), round(error_muestreo,4)

def calcular_tamano_muestra_t_iterativo(s, error_muestreo, confianza=0.95, tol=1e-6, max_iter=100):
    alpha = 1 - confianza
    n = 2  # valor inicial
    
    for _ in range(max_iter): #metodo iterativo
        df = n - 1 #grados de libertad
        t_critico = t.ppf(1 - alpha/2, df)
        n_nuevo = (t_critico * s / error_muestreo) ** 2
        n_nuevo = max(2, n_nuevo)  # asegura mínimo 2
        
        if abs(n_nuevo - n) < tol:
            break
        
        n = n_nuevo
    
    return math.ceil(n)


# uso
resultado, error_muestreo = intervalo_confianza_t(x_bar=15.25, s=7.3767, n=20, confianza=0.90)
print(f"Intervalo de confianza: {resultado}")
print(f"Error de muestreo: {error_muestreo}")

# uso(cuando pide saber el tamaño de n cuando pasa)
s = 7.3767
error_deseado = 1.4259 #la mitad del error anterior
confianza = 0.90

n_requerido = calcular_tamano_muestra_t_iterativo(s, error_deseado, confianza)
print(f"Tamaño de muestra necesario (método iterativo solo con t): {n_requerido}")