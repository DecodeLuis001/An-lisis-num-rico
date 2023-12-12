import math

def calcular_senox_taylor(x, n):
    """
    Calcula sin(x) utilizando la serie de Taylor hasta el n-ésimo término.

    Parameters:
    - x: Ángulo en radianes.
    - n: Número de términos en la serie de Taylor.

    Returns:
    - Aproximación de sin(x) utilizando la serie de Taylor.
    """
    sin_x_aprox = 0.0

    for k in range(n):
        coeficiente = (-1)**k / math.factorial(2*k + 1)
        termino = coeficiente * x**(2*k + 1)
        sin_x_aprox += termino

    return sin_x_aprox

# Ejemplo de uso:
angulo_radianes = math.pi / 4  # 45 grados en radianes
terminos_serie_taylor = 10

# Calcular sin(x) usando la serie de Taylor
sin_x_aproximado = calcular_senox_taylor(angulo_radianes, terminos_serie_taylor)

# Mostrar resultados
print(f"Aproximación de sin(x) usando {terminos_serie_taylor} términos: {sin_x_aproximado}")
print(f"Valor real de sin(x): {math.sin(angulo_radianes)}")
