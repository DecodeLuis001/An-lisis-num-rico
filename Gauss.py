import numpy as np

def eliminacion_gaussiana(A, b):
    """
    Método de Eliminación de Gauss para resolver un sistema de ecuaciones lineales Ax = b.

    Parameters:
    - A: Matriz de coeficientes del sistema.
    - b: Vector de términos independientes.

    Returns:
    - x: Vector solución.
    """
    n = len(b)

    # Construir la matriz aumentada [A|b]
    sistema_extendido = np.column_stack((A, b))

    # Aplicar eliminación hacia adelante
    for i in range(n):
        # Hacer el coeficiente diagonal 1
        divisor = sistema_extendido[i, i]
        sistema_extendido[i, :] /= divisor

        # Hacer ceros en la columna debajo de la diagonal
        for j in range(i + 1, n):
            factor = sistema_extendido[j, i]
            sistema_extendido[j, :] -= factor * sistema_extendido[i, :]

    # Aplicar sustitución hacia atrás
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = sistema_extendido[i, -1] - np.dot(sistema_extendido[i, i+1:n], x[i+1:])

    return x

# Ejemplo de uso:
A = np.array([[2, -1, 1],
              [1, 1, -1],
              [3, 2, 3]])

b = np.array([8, 0, 3])

solucion = eliminacion_gaussiana(A, b)
print(f"Solución del sistema: {solucion}")
