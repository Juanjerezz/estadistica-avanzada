import math
from scipy.stats import t

def test_hipotesis_varianzas(s1, s2, n1, n2, alpha=0.05):
    F = (s1**2) / (s2**2)
    gl1 = n1 - 1
    gl2 = n2 - 1

    F_crit_inf = t.ppf(alpha/2, gl1)
    F_crit_sup = t.ppf(1 - alpha/2, gl1)
    from scipy.stats import f
    F_inf = f.ppf(alpha/2, gl1, gl2)
    F_sup = f.ppf(1 - alpha/2, gl1, gl2)

    iguales = F_inf <= F <= F_sup
    return iguales, F, (F_inf, F_sup)

def test_hipotesis_medias(x1, s1, n1, x2, s2, n2, alpha=0.05, tipo="bilateral"):
    iguales, F, (F_inf, F_sup) = test_hipotesis_varianzas(s1, s2, n1, n2, alpha)

    if iguales:
        # Caso 2
        sp2 = ((n1 - 1)*s1**2 + (n2 - 1)*s2**2) / (n1 + n2 - 2)
        sp = math.sqrt(sp2)
        t_stat = (x1 - x2) / (sp * math.sqrt(1/n1 + 1/n2))
        gl = n1 + n2 - 2
    else:
        # Caso 3
        t_stat = (x1 - x2) / math.sqrt(s1**2/n1 + s2**2/n2)
        gl_num = (s1**2/n1 + s2**2/n2)**2
        gl_den = ((s1**2/n1)**2 / (n1 - 1)) + ((s2**2/n2)**2 / (n2 - 1))
        gl = gl_num / gl_den

    # calculo valor critico
    if tipo == "bilateral":
        t_crit = t.ppf(1 - alpha/2, gl)
        rechazar = abs(t_stat) > t_crit
    elif tipo == "cola_izquierda":
        t_crit = t.ppf(alpha, gl)
        rechazar = t_stat < t_crit
    else: 
        t_crit = t.ppf(1 - alpha, gl)
        rechazar = t_stat > t_crit

    return {
        "varianzas_iguales": iguales,
        "F": F,
        "F_intervalo": (F_inf, F_sup),
        "t_stat": t_stat,
        "gl": gl,
        "t_crit": t_crit,
        "rechazar_H0": rechazar
    }

#uso
resultado = test_hipotesis_medias(
    x1=5.2, s1=1.1, n1=30,
    x2=4.8, s2=1.3, n2=28,
    alpha=0.05, tipo="bilateral"
)

print(resultado)