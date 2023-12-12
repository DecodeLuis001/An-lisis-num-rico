import math

def calcular_cosx_taylor(x, n):
    """
    Calcula cos(x) utilizando la serie de Taylor hasta el n-ésimo término.

    Parameters:
    - x: Ángulo en radianes.
    - n: Número de términos en la serie de Taylor.

    Returns:
    - Aproximación de cos(x) utilizando la serie de Taylor.
    """
    cos_x_aprox = 0.0

    for k in range(n):
        coeficiente = (-1)**k / math.factorial(2*k)
        termino = coeficiente * x**(2*k)
        cos_x_aprox += termino

    return cos_x_aprox

# Ejemplo de uso:
angulo_radianes = math.pi / 4  # 45 grados en radianes
terminos_serie_taylor = 10

# Calcular cos(x) usando la serie de Taylor
cos_x_aproximado = calcular_cosx_taylor(angulo_radianes, terminos_serie_taylor)

# Mostrar resultados
print(f"Aproximación de cos(x) usando {terminos_serie_taylor} términos: {cos_x_aproximado}")
print(f"Valor real de cos(x): {math.cos(angulo_radianes)}")
