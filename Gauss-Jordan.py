import numpy as np

def gauss_jordan(A, b=None):
    """
    Método de Gauss-Jordan para resolver un sistema de ecuaciones lineales o encontrar la inversa de una matriz.

    Parameters:
    - A: Matriz de coeficientes del sistema o matriz a invertir.
    - b: Vector de términos independientes (opcional).

    Returns:
    - Si b es proporcionado, la función devuelve el vector solución del sistema.
    - Si b no es proporcionado, la función devuelve la matriz inversa de A.
    """
    if b is not None:
        # Construir la matriz aumentada [A|b]
        sistema_extendido = np.column_stack((A, b))
    else:
        # Si no se proporciona b, A es la matriz que se va a invertir
        sistema_extendido = np.hstack((A, np.identity(len(A))))

    n = len(sistema_extendido)

    # Aplicar eliminación hacia adelante
    for i in range(n):
        # Hacer el coeficiente diagonal 1
        divisor = sistema_extendido[i, i]
        sistema_extendido[i, :] /= divisor

        # Hacer ceros en la columna debajo y encima de la diagonal
        for j in range(n):
            if i != j:
                factor = sistema_extendido[j, i]
                sistema_extendido[j, :] -= factor * sistema_extendido[i, :]

    if b is not None:
        # Devolver el vector solución
        return sistema_extendido[:, -1]
    else:
        # Devolver la matriz inversa
        return sistema_extendido[:, n:]


# Ejemplo de uso para resolver un sistema de ecuaciones lineales:
A = np.array([[2, -1, 1],
              [1, 1, -1],
              [3, 2, 3]])

b = np.array([8, 0, 3])

solucion = gauss_jordan(A, b)
print(f"Solución del sistema: {solucion}")

# Ejemplo de uso para encontrar la inversa de una matriz:
matriz_a_invertir = np.array([[1, 2, 3],
                              [0, 1, 4],
                              [5, 6, 0]])

inversa = gauss_jordan(matriz_a_invertir)
print(f"Inversa de la matriz:\n{inversa}")
