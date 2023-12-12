import numpy as np

def diferencias_divididas(x, y):
    """
    Calcula las diferencias divididas para el método de interpolación de Newton.

    Parameters:
    - x: Lista de coordenadas x de los puntos conocidos.
    - y: Lista de coordenadas y correspondientes a los puntos conocidos.

    Returns:
    - Matriz de diferencias divididas.
    """
    n = len(x)
    matriz_diferencias = np.zeros((n, n))

    # Inicializar la primera columna con los valores y conocidos
    matriz_diferencias[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            matriz_diferencias[i, j] = (matriz_diferencias[i + 1, j - 1] - matriz_diferencias[i, j - 1]) / (x[i + j] - x[i])

    return matriz_diferencias

def interpolacion_newton(x_interp, x, y):
    """
    Método de interpolación de Newton para encontrar el valor interpolado en un punto específico.

    Parameters:
    - x_interp: Punto en el cual se desea interpolar.
    - x: Lista de coordenadas x de los puntos conocidos.
    - y: Lista de coordenadas y correspondientes a los puntos conocidos.

    Returns:
    - y_interp: Valor interpolado en el punto x_interp.
    """
    n = len(x)
    diferencias = diferencias_divididas(x, y)
    y_interp = diferencias[0, 0]

    for i in range(1, n):
        termino = 1

        for j in range(i):
            termino *= (x_interp - x[j])

        y_interp += diferencias[0, i] * termino

    return y_interp

# Ejemplo de uso:
x_datos = np.array([1, 2, 4])
y_datos = np.array([3, 1, 2])

# Punto en el cual se desea interpolar
x_interp = 3

# Aplicar el método de interpolación de Newton
y_interp = interpolacion_newton(x_interp, x_datos, y_datos)

print(f"Valor interpolado en x={x_interp}: {y_interp}")
