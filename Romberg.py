import numpy as np

def metodo_romberg(f, a, b, n):
    """
    Método de Romberg para aproximar la integral definida de una función.

    Parameters:
    - f: Función a integrar.
    - a: Límite inferior de integración.
    - b: Límite superior de integración.
    - n: Número de niveles en la extrapolación de Richardson.

    Returns:
    - Aproximación de la integral definida.
    """
    # Inicializar la matriz de Romberg con ceros
    R = np.zeros((n, n))

    # Calcular la aproximación de la integral usando la regla del trapecio compuesta
    h = b - a
    R[0, 0] = 0.5 * h * (f(a) + f(b))

    for i in range(1, n):
        h /= 2
        suma = 0

        for k in range(1, 2**i, 2):
            suma += f(a + k * h)

        R[i, 0] = 0.5 * R[i-1, 0] + h * suma

        # Calcular las correcciones usando la extrapolación de Richardson
        for j in range(1, i+1):
            R[i, j] = R[i, j-1] + (R[i, j-1] - R[i-1, j-1]) / (4**j - 1)

    return R[n-1, n-1]

# Ejemplo de uso:
def funcion_a_integrar(x):
    """
    Función de ejemplo a integrar.

    Parameters:
    - x: Variable de la función.

    Returns:
    - Valor de la función en x.
    """
    return x**2

# Límites de integración
a = 0
b = 2

# Número de niveles en la extrapolación de Richardson
niveles_romberg = 4

# Aplicar el método de Romberg
resultado_integral = metodo_romberg(funcion_a_integrar, a, b, niveles_romberg)

# Mostrar resultados
print(f"Aproximación de la integral definida: {resultado_integral}")
