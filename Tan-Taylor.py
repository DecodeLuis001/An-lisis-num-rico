import math

def calcular_tanx_taylor(x, n):
    """
    Calcula tan(x) utilizando la serie de Taylor hasta el n-ésimo término.

    Parameters:
    - x: Ángulo en radianes.
    - n: Número de términos en la serie de Taylor.

    Returns:
    - Aproximación de tan(x) utilizando la serie de Taylor.
    """
    tan_x_aprox = 0.0

    for k in range(1, n+1):
        coeficiente = 1 if k % 2 == 1 else 0
        coeficiente *= 2 * k - 1
        termino = coeficiente * (2**(2*k - 1) - 1) * math.factorial(2*k - 1) * x**(2*k - 1)
        tan_x_aprox += termino

    return tan_x_aprox

# Ejemplo de uso:
angulo_radianes = math.pi / 4  # 45 grados en radianes
terminos_serie_taylor = 10

# Calcular tan(x) usando la serie de Taylor
tan_x_aproximado = calcular_tanx_taylor(angulo_radianes, terminos_serie_taylor)

# Mostrar resultados
print(f"Aproximación de tan(x) usando {terminos_serie_taylor} términos: {tan_x_aproximado}")
print(f"Valor real de tan(x): {math.tan(angulo_radianes)}")
