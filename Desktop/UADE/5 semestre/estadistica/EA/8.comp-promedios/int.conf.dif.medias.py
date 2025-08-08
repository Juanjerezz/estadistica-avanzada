import math
from scipy.stats import t
from scipy.stats import f

def intervalo_confianza_varianzas(s1, s2, n1, n2, alpha=0.05):
    F = (s1**2) / (s2**2)
    gl1 = n1 - 1
    gl2 = n2 - 1

    F_inf = f.ppf(alpha/2, gl1, gl2)
    F_sup = f.ppf(1 - alpha/2, gl1, gl2)

    iguales = F_inf <= F <= F_sup
    return iguales

def intervalo_confianza_diferencia_medias(x1, s1, n1, x2, s2, n2, confianza=0.95):
    alpha = 1 - confianza
    iguales = intervalo_confianza_varianzas(s1, s2, n1, n2, alpha)

    if iguales:
        # caso 2
        sp2 = ((n1 - 1)*s1**2 + (n2 - 1)*s2**2) / (n1 + n2 - 2)
        sp = math.sqrt(sp2)
        error = t.ppf(1 - alpha/2, n1 + n2 - 2) * sp * math.sqrt(1/n1 + 1/n2)
        gl = n1 + n2 - 2
    else:
        # caso 3
        error = t.ppf(1 - alpha/2, 
                      ((s1**2/n1 + s2**2/n2)**2) /
                      ((s1**2/n1)**2 / (n1 - 1) + (s2**2/n2)**2 / (n2 - 1))
                     ) * math.sqrt(s1**2/n1 + s2**2/n2)
        gl = ((s1**2/n1 + s2**2/n2)**2) / \
             ((s1**2/n1)**2 / (n1 - 1) + (s2**2/n2)**2 / (n2 - 1))

    diff = x1 - x2
    li = diff - error
    ls = diff + error

    return (round(li, 4), round(ls, 4)), round(error, 4), iguales, round(gl, 2)

#uso
intervalo, error, iguales, gl = intervalo_confianza_diferencia_medias(
    x1=5.2, s1=1.1, n1=30,
    x2=4.8, s2=1.3, n2=28,
    confianza=0.95
)

print("Intervalo de confianza para la diferencia de medias:", intervalo)
print("Error de muestreo:", error)
print("Varianzas iguales:", iguales)
print("Grados de libertad:", gl)