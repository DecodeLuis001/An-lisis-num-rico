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

def derivada_funcion(x):
    """
    Definición de la derivada de la función objetivo.

    La derivada es esencial para el método de Newton-Raphson.

    Parameters:
    - x: Valor en el que evaluar la derivada.

    Returns:
    - Valor de la derivada en x.
    """
    # Ejemplo: Derivada de la función cuadrática
    return 2 * x

def metodo_newton_raphson(x0, tol=1e-6, max_iter=100):
    """
    Método de Newton-Raphson para encontrar raíces de una función.

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
        f_x0 = funcion_objetivo(x0)
        f_prime_x0 = derivada_funcion(x0)

        if abs(f_prime_x0) < 1e-10:
            raise ValueError("La derivada se hace muy pequeña. Posiblemente no hay raíces o la convergencia es lenta.")

        x1 = x0 - f_x0 / f_prime_x0

        if abs(x1 - x0) < tol:
            break

        x0 = x1
        iterations += 1

    return x1, iterations

# Ejemplo de uso:
punto_inicial = 2.0
raiz_aproximada, num_iteraciones = metodo_newton_raphson(punto_inicial)

print(f"Aproximación de la raíz: {raiz_aproximada}")
print(f"Número de iteraciones: {num_iteraciones}")
