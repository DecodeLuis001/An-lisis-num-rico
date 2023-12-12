def funcion_objetivo(x):
    """
    Definición de la función objetivo.

    En estadística y probabilidad, esta función podría representar
    una distribución de probabilidad acumulativa o una función de densidad de probabilidad.
    Ajusta la función según tus necesidades.

    Parameters:
    - x: Valor en el que evaluar la función.

    Returns:
    - Valor de la función en x.
    """
    # Ejemplo: Función cuadrática
    return x**2 - 4

def funcion_punto_fijo(x):
    """
    Definición de la función de punto fijo.

    La función de punto fijo se elige para transformar la ecuación f(x) = 0 en
    una ecuación equivalente x = g(x).

    Parameters:
    - x: Valor en el que evaluar la función.

    Returns:
    - Valor de la función en x.
    """
    # Ejemplo: Función de punto fijo asociada a la función cuadrática
    return (x**2 + 4) / (2 * x)

def metodo_punto_fijo(x0, tol=1e-6, max_iter=100):
    """
    Método del Punto Fijo para encontrar raíces de una función.

    Parameters:
    - x0: Punto inicial.
    - tol: Tolerancia para detener el método (por defecto, 1e-6).
    - max_iter: Número máximo de iteraciones (por defecto, 100).

    Returns:
    - root: Aproximación de la raíz.
    - iterations: Número de iteraciones realizadas.
    """
    iterations = 0

    while iterations < max_iter:
        x1 = funcion_punto_fijo(x0)

        if abs(x1 - x0) < tol:
            break

        x0 = x1
        iterations += 1

    return x1, iterations

# Ejemplo de uso:
punto_inicial = 1.0
raiz_aproximada, num_iteraciones = metodo_punto_fijo(punto_inicial)

print(f"Aproximación de la raíz: {raiz_aproximada}")
print(f"Número de iteraciones: {num_iteraciones}")
