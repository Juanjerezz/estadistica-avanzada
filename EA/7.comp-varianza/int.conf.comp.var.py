import math
from scipy.stats import f  # Distribución Fisher

def intervalo_confianza_varianzas(s1, s2, n1, n2, confianza=0.95):
    razon = s1**2 / s2**2
    
    df1 = n1 - 1
    df2 = n2 - 1
    
    alpha = 1 - confianza
    f_inf = f.ppf(alpha / 2, df1, df2)
    f_sup = f.ppf(1 - alpha / 2, df1, df2)
    
    li = razon / f_sup
    ls = razon / f_inf
    error = (ls - li) / 2
    
    return (round(li, 4), round(ls, 4)), round(error, 4) 

def intervalo_confianza_desvios(s1, s2, n1, n2, confianza=0.95):
    razon = s1 / s2  

    df1 = n1 - 1
    df2 = n2 - 1

    alpha = 1 - confianza
    f_inf = f.ppf(alpha / 2, df1, df2)
    f_sup = f.ppf(1 - alpha / 2, df1, df2)

    li = razon / math.sqrt(f_sup)
    ls = razon / math.sqrt(f_inf)
    error = (ls - li) / 2

    return (round(li, 4), round(ls, 4)), round(error, 4)

intervalo_var, error_var = intervalo_confianza_varianzas(
    s1=4.2,
    s2=3.6,
    n1=15,
    n2=12,
    confianza=0.95
)

intervalo_std, error_std = intervalo_confianza_desvios(
    s1=4.2,
    s2=3.6,
    n1=15,
    n2=12,
    confianza=0.95
)

print("Intervalo de confianza para la razón de varianzas:", intervalo_var)
print("Error de muestreo (varianzas):", error_var)
print("Intervalo de confianza para la razón de desvíos estándar:", intervalo_std)
print("Error de muestreo (desvíos):", error_std)