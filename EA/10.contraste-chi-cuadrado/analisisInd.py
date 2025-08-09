import pandas as pd
from scipy.stats import chi2_contingency

def analisis_independencia(tabla, alpha=0.05, mostrar_resultado=True):  
    chi2, p_valor, dof, tabla_esperada = chi2_contingency(tabla)

    resultado = {
        "Chi2": chi2,
        "p-valor": p_valor,
        "Grados de libertad": dof,
        "Frecuencias esperadas": tabla_esperada
    }
    
    if mostrar_resultado:
        print(f"Chi-cuadrado: {chi2:.4f}")
        print(f"p-valor: {p_valor:.4f}")
        print(f"Grados de libertad: {dof}")
        print("Frecuencias esperadas:\n", pd.DataFrame(tabla_esperada))
        
        if p_valor < alpha:
            print("\nConclusión: Se rechaza H0 → Existe asociación entre las variables.")
        else:
            print("\nConclusión: No se rechaza H0 → No existe asociación entre las variables.")
    
    return resultado

#uso
datos = pd.DataFrame({
    'Fuma': [30, 10],
    'No fuma': [20, 40]
}, index=['Enfermo', 'Sano'])

analisis_independencia(datos, alpha=0.05)