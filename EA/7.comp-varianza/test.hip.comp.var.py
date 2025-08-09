import math
from scipy.stats import f 

def test_hipotesis_varianzas(s1, s2, n1, n2, alpha=0.05, tipo='bilateral'):
    F_stat = (s1**2) / (s2**2)
    df1 = n1 - 1
    df2 = n2 - 1

    if tipo == 'bilateral':
        F_crit_inf = f.ppf(alpha / 2, df1, df2)
        F_crit_sup = f.ppf(1 - alpha / 2, df1, df2)
        p_value = 2 * min(f.cdf(F_stat, df1, df2), 1 - f.cdf(F_stat, df1, df2))
        rechazo = F_stat < F_crit_inf or F_stat > F_crit_sup

        return {
            'F': round(F_stat, 4),
            'F_critico_inferior': round(F_crit_inf, 4),
            'F_critico_superior': round(F_crit_sup, 4),
            'p_value': round(p_value, 4),
            'razon_varianzas': round(F_stat, 4),
            'rechazar_H0': rechazo
        }

    elif tipo == 'derecha':
        F_crit_sup = f.ppf(1 - alpha, df1, df2)
        p_value = 1 - f.cdf(F_stat, df1, df2)
        rechazo = F_stat > F_crit_sup

        return {
            'F': round(F_stat, 4),
            'F_critico': round(F_crit_sup, 4),
            'p_value': round(p_value, 4),
            'razon_varianzas': round(F_stat, 4),
            'rechazar_H0': rechazo
        }

    elif tipo == 'izquierda':
        F_crit_inf = f.ppf(alpha, df1, df2)
        p_value = f.cdf(F_stat, df1, df2)
        rechazo = F_stat < F_crit_inf

        return {
            'F': round(F_stat, 4),
            'F_critico': round(F_crit_inf, 4),
            'p_value': round(p_value, 4),
            'razon_varianzas': round(F_stat, 4),
            'rechazar_H0': rechazo
        }

    else:
        raise ValueError("Tipo debe ser 'bilateral', 'derecha' o 'izquierda'.")


resultado = test_hipotesis_varianzas(
    s1=4.2,   
    s2=3.6,
    n1=15,
    n2=12,
    alpha=0.05,
    tipo='bilateral'
)

print("Resultado del test para comparación de varianzas:")
for clave, valor in resultado.items():
    print(f"{clave}: {valor}")